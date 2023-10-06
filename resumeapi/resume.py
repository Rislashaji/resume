import os
import re
import spacy
from PyPDF2 import PdfReader
from docx import Document
nlp = spacy.load('en_core_web_sm')
from resumeapi.models import*
from resumedetector.models import*
from resumedetector.views import* 
from django.http import HttpRequest
import requests

# Load the spaCy model 

nlp = spacy.load("en_core_web_sm")


# predefined_skills = ["ios", "c++", "Machine Learning", "Data Analysis", "Android"]

predefined_skills,company = resume_skill()
print("predefined_skills......",predefined_skills)

def extract_skills(text):
    extracted_skills = []
    skill_pattern = r'\b(?:' + '|'.join(re.escape(skill) for skill in predefined_skills) + r')\b'
    matches = re.findall(skill_pattern, text, flags=re.IGNORECASE)
    for match in matches:
        extracted_skills.append(match.title())
    return list(set(extracted_skills))


def parse_pdf(pdf_path):
    skills = []
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text = page.extract_text()
        skills += extract_skills(text)
    return skills

# Function to parse Word document

def parse_word_doc(docx_path):
    skills = []
    doc = Document(docx_path)
    for paragraph in doc.paragraphs:
        text = paragraph.text
        skills += extract_skills(text)
    return skills

# Function to parse a single resume

def parse_resume(resume_path):
    _, file_extension = os.path.splitext(resume_path)
    if file_extension.lower() == ".pdf":
        skills = parse_pdf(resume_path)
    elif file_extension.lower() == ".docx":
        skills = parse_word_doc(resume_path)
    else:
        raise ValueError("Unsupported file format")
    return skills

# Function to process all resumes in a folder

def process_resumes_in_folder(folder_path):
    matching_skills_all_resumes = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith((".pdf", ".docx")):
                resume_path = os.path.join(root, file)
                matching_skills = parse_resume(resume_path)
                matching_skills_all_resumes[resume_path] = matching_skills
                print('matching_skills_all_resumes',matching_skills_all_resumes)
    return matching_skills_all_resumes

#resume path
def resume(image):
    folder_path = "image"
    matching_skills_all_resumes = process_resumes_in_folder(folder_path)


    for resume_path, matching_skills in matching_skills_all_resumes.items():
        num_predefined_skills = len(predefined_skills)
        num_matching_skills = len(matching_skills)
        print("Resume:", resume_path)
        print("Number of Predefined Skills:", num_predefined_skills)
        print("Number of Matching Skills:", num_matching_skills)
        print("Matching Skills:", matching_skills)


    classification_result = tb_skill(skill=matching_skills)
    classification_result.save()

    return  resume_path,  num_predefined_skills ,num_matching_skills, matching_skills
 
       
def main():
    result = resume()
    return result     