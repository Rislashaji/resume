from django.shortcuts import render
from.models import*
from .serializers import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .resume import *
from django.http import JsonResponse
from resumedetector.models import*
import ast


# Create your views here.


@api_view(['GET'])
def getregister(request):
	data=tb_register.objects.all()
	serializer = RegisterSerializer(data, many=True)
	response_data = {"data":serializer.data}
	return Response(response_data)


@api_view(['POST'])
def addregister(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_data = {"data":[{"status":"success","data":serializer.data}]}
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        response_data = {"status": "error"}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
	
@api_view(['POST'])
def userlogin(request):
    email = request.data.get('email')
    pswd = request.data.get('pswd')
    
    try:
        users = tb_register.objects.filter(email=email, pswd=pswd)
        
        if users.exists():
            user = users.first()
            
            response_data ={"data":[{
                "status": "success",
                "message": "Login successful",
                "id":user.id,
                "username": user.uname,
                "email": user.email,
                "name": user.name,
				"phone":user.phn
            }]}
            return Response(response_data)
        else:
           
            response_data =[ {"status": "error", "message": "Invalid credentials", "username": ""}]
            return Response(response_data)
    except tb_register.DoesNotExist:
      
        response_data = {"status": "error", "message": "Invalid credentials", "username": ""}
        return Response(response_data)      
    

@api_view(['POST'])
def uploadresume(request):
    if request.method == "POST":
        id = int(request.data.get('user_id'))
        image = request.FILES.get('image')
        if image is not None:
            user_instance = tb_register.objects.get(id=id)
            data = tb_resume(user_id=user_instance, image=image)
            data.save()
            image_url = data.image.url
            result = resume(image_url)
            latest_skill_instance = tb_skill.objects.latest('id')
            latest_skill_instance.user_id = user_instance
            latest_skill_instance.save()
            return Response({"message": "success"})
        else:
            return Response({"error": "Image not provided"})
    else:
        return Response({"error": "Invalid request method"}) 
    

    
@api_view(['POST'])
def profile(request):
    user_id = request.data.get('user_id') 
    try:
        instance = tb_register.objects.get(id=user_id)
    except tb_register.DoesNotExist:
        return Response({"error": "User not found"})

    serializer = ProfileSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        response_data = {"status": "success"}
        return Response(response_data, status=status.HTTP_200_OK)
    else:
        response_data = {"status": "error", "errors": serializer.errors}
        return Response(response_data)


@api_view(['POST'])
def get_profile(request):
    user_id = request.data.get('user_id') 
    try:
        user = tb_register.objects.filter(id=user_id)
        serializer = GetProfileSerializer(user, many=True)
        response_data = {"data": serializer.data}
        return Response(response_data)
    except tb_register.DoesNotExist:
        response_data = {"error": "User orders not found"}
        return Response(response_data)


@api_view(['POST'])
def edit_profile(request):
        if request.method == "POST":
            user_id = request.data.get("id")
            qualification = request.data.get("qualification")
            yop = request.data.get("yop")
            dob = request.data.get("dob")
            location = request.data.get("location")
            email = request.data.get("email")
            phn = request.data.get("phn")
            name = request.data.get("name")
            var=tb_register.objects.all().filter(id=user_id).update(qualification=qualification,yop=yop,dob=dob,location=location,email=email,phn=phn,name=name)
            aa=tb_register.objects.all().filter(id=user_id)
            serializer = GetProfileSerializer(aa, many=True)
            return Response({"status": 'success'},)  
        else:
            return Response({"status": "error", "data": serializer.errors},)
        

@api_view(['POST'])
def apply_job(request):
    status = 'Applied'
    job_id = request.data.get('job_id')
    user_id = request.data.get('user_id')
    try:
        job_instance = tb_details.objects.get(id=job_id)
        user_instance = tb_register.objects.get(id=user_id)
        cmpny_id = job_instance.cmpny_id  
    except tb_details.DoesNotExist:
        return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
    except tb_register.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    data = tb_job_application(user_id=user_instance, job_id=job_instance, status=status, cmpny_id=cmpny_id)
    data.save()
    response_data = {"message": "success"}
    return Response(response_data)



@api_view(['POST'])
def list_company(request):
    id = request.data.get('user_id')
    try:
        last_skill = tb_skill.objects.filter(user_id=id).values_list('skill', flat=True).last()
        if not last_skill:
            return Response({"matched_companies": []})
        skill_dict = ast.literal_eval(last_skill)
        matching_companies = []
        for job in skill_dict:
            companies = tb_details.objects.filter(skill=job)
            matching_companies.extend(companies)

        serialized_companies = CompanySerializer(matching_companies, many=True).data
        response_data = {"matched_companies": serialized_companies}

        for company in serialized_companies:
            company["status"] = tb_job_application.objects.filter(user_id=id).values_list('status', flat=True).last() or ""
    except Exception as e:
        print(str(e))
        serialized_companies = []

    return Response(response_data)


@api_view(['POST'])
def view_approved_job(request):
    user_id = request.data.get('user_id') 
    job_applications = tb_job_application.objects.filter(status='Approved',user_id=user_id).select_related('job_id', 'user_id')
    serializer = ApprovedSerializer(job_applications, many=True)
    response_data = {"data":serializer.data}
    return Response(response_data)