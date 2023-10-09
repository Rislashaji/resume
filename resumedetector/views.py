from django.shortcuts import render,redirect
from.models import*
from resumeapi.models import*
from django.http import HttpRequest
from django.core.serializers import serialize
from django.http import JsonResponse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')


def company_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phn=request.POST.get('phn')
        uname=request.POST.get('uname')
        pswd=request.POST.get('pswd')
        email=request.POST.get('email')
        adrs=request.POST.get('adrs')
        data1=tb_cmpny_register(name=name,uname=uname,phn=phn,email=email,pswd=pswd,adrs=adrs)
        data1.save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')



def admin_reg(request):
    if request.method=='POST':
        pswd=request.POST.get('pswd')
        email=request.POST.get('email')
        data1=tb_cmpny_register(email=email,pswd=pswd,utype="Admin")
        data1.save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')


def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        pswd = request.POST['pswd']
        
        # Check if the user with provided email, password, and utype=admin exists
        var = tb_cmpny_register.objects.filter(email=email, pswd=pswd, utype='Admin').first()
        
        if var:
            # Set session id if user with specified utype is found
            request.session['id'] = var.id
            return redirect('dashboard')
        else:
            return render(request, 'admin_login.html', {'msg': 'Sorry, invalid credentials'})
    else:
        return render(request, 'admin_login.html')

def admin_logout(request):
    if request.user.is_authenticated and request.user.utype == 'admin':
        logout(request)
        return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html') 




def add_details(request):
    if request.method=='POST':
        id=request.session['id']
        name=request.POST.get('name')
        skill=request.POST.get('skill')
        qualification=request.POST.get('qualification')
        email=request.POST.get('email')
        job=request.POST.get('job')
        date=request.POST.get('date')
        description=request.POST.get('descr')
        location=request.POST.get('adrs')
        instance = tb_cmpny_register.objects.get(id=id)
        data1=tb_details(cmpny_id=instance,name=name,skill=skill,qualification=qualification,email=email,job=job,date=date,description=description,location=location)
        data1.save()
        return render(request,'add_details.html')
    else:
        return render(request,'add_details.html')


def detail_table(request):
    id=request.session['id']
    data=tb_details.objects.filter(cmpny_id=id)
    return render(request,'details_table.html',{'data':data})

def edit(request,id):
    data=tb_details.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})

def update(request,id):
    if request.method=='POST':
        name=request.POST.get('name')
        skill=request.POST.get('skill')
        qualification=request.POST.get('qualification')
        email=request.POST.get('email')
        job=request.POST.get('job')
        date=request.POST.get('date')
        description=request.POST.get('descr')
        location=request.POST.get('adrs')
        tb_details.objects.filter(id=id).update(name=name,skill=skill,qualification=qualification,email=email,job=job,date=date,description=description,location=location)
        return redirect('detail_table')
    else:
        return render(request,'edit.html') 
    
def delete(request,id):
    tb_details.objects.filter(id=id).delete()
    return redirect('detail_table')

def register(request):
    return render(request,'register.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pswd = request.POST['pswd']
        var = tb_cmpny_register.objects.all().filter(
            email=email, pswd=pswd)
        
        if var:
            for x in var:
                request.session['id'] = x.id
            return redirect('recruitment_dashboard')
        else:
            return render(request, 'login.html',{'msg':'sorry invalid'})
    else:
        return render(request, 'login.html')

def view_resume(request):
    data=tb_resume.objects.all()
    return render(request,'view_resume.html',{'data':data})

def resume_skill():
    entries = tb_details.objects.values('id', 'skill')  
    skills = [entry['skill'] for entry in entries] 
    print("resume_skill......",skills) 
    ids = [entry['id'] for entry in entries] 
    return skills, ids

def recruitment_dashboard(request):
    return render(request,'recruitment_dashboard.html')


def view_applied_job(request):
    user_id = request.session.get('id')
    job_applications = tb_job_application.objects.filter(cmpny_id=user_id, status='applied').select_related('job_id', 'user_id')
    return render(request, 'view_applied_job.html', {"data": job_applications})


def approve_application(request, id):
    if request.method == "POST":
        tb_job_application.objects.filter(id=id).update(status='Approved')
        return redirect('view_applied_job')
    return render(request, 'view_applied_job.html')


def view_users(request):
    data=tb_register.objects.all()
    return render(request,'view_users.html',{'data':data})


def view_recruiters(request):
    data1 = tb_cmpny_register.objects.exclude(utype='admin')
    return render(request, 'view_recruiters.html', {'data1': data1})


def logout(request):
    if request.session.has_key('id'):
        del request.session['id']
        logout(request)
    return render(request,'login.html')