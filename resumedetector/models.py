from django.db import models


# Create your models here.

class tb_cmpny_register(models.Model):
    email=models.EmailField(max_length=100,default="")
    phn=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    uname=models.CharField(max_length=100,default="")
    pswd=models.CharField(max_length=100,default="")
    adrs=models.CharField(max_length=100,default="")
    utype=models.CharField(max_length=100,default="")
   
   
class tb_register(models.Model):
    email=models.EmailField(max_length=100,default="")
    phn=models.CharField(max_length=100,default="")
    name=models.CharField(max_length=100,default="")
    uname=models.CharField(max_length=100,default="")
    pswd=models.CharField(max_length=100,default="")
    qualification=models.CharField(max_length=100,default="")
    yop=models.CharField(max_length=100,default="") #year of passing
    dob=models.CharField(max_length=100,default="")
    location=models.CharField(max_length=100,default="")

class tb_resume(models.Model):
    image=models.ImageField(upload_to='image',default='null.jpeg')   
    user_id=models.ForeignKey(tb_register,on_delete=models.CASCADE,blank=True,null=True)


class tb_skill(models.Model):
    skill=models.CharField(max_length=100,default="") 
    user_id=models.ForeignKey(tb_register,on_delete=models.CASCADE,blank=True,null=True)

# job details
class tb_details(models.Model):
    name=models.CharField(max_length=100,default="")
    skill=models.CharField(max_length=100,default="")
    qualification=models.CharField(max_length=100,default="")
    email=models.EmailField(max_length=100,default="")
    date=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    location=models.CharField(max_length=100,default="")
    job=models.CharField(max_length=100,default="")
    cmpny_id=models.ForeignKey(tb_cmpny_register,on_delete=models.CASCADE,blank=True,null=True)
    user_id=models.ForeignKey(tb_register,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=100,default="")


class tb_job_application(models.Model):
    job_id=models.ForeignKey(tb_details,on_delete=models.CASCADE,blank=True,null=True)
    cmpny_id=models.ForeignKey(tb_cmpny_register,on_delete=models.CASCADE,blank=True,null=True)
    user_id=models.ForeignKey(tb_register,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length=100,default="")

    
    


