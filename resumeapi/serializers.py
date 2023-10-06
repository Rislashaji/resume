from rest_framework import serializers
from resumeapi.models import*
from resumedetector.models import*



class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_register
		fields=('id','email','phn','name','uname','pswd')


class ResumeSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_resume
		fields='__all__'	

class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_skill
		fields='__all__'			


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_details
		exclude = ('qualification','user_id')  		


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_register
		fields=('qualification','yop','dob','location')	


class GetProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_register
		fields=('qualification','yop','dob','location','email','phn','name')	


class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_job_application
		fields = '__all__'	

class IdSerializer(serializers.ModelSerializer):
	class Meta:
		model=tb_register
		fields=['id']	
