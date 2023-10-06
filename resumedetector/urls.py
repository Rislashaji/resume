from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    
    path('dashboard/', views.dashboard, name="dashboard"),
    path('company_reg/', views.company_reg, name="company_reg"),
    path('add_details/', views.add_details, name="add_details"),
    path('table/', views.detail_table, name="detail_table"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('view_resume/', views.view_resume, name="view_resume"),
    path('resume_skill/<int:id>', views.resume_skill, name="resume_skill"),
    path('recruitment_dashboard/', views.recruitment_dashboard, name="recruitment_dashboard"),
    path('view_applied_job/', views.view_applied_job, name="view_applied_job"),

]