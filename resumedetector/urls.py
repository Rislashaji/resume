from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    
    path('dashboard/', views.dashboard, name="dashboard"),
    path('company_reg/', views.company_reg, name="company_reg"),
    path('admin_reg/', views.admin_reg, name="admin_reg"),
    path('admin_login/', views.admin_login, name="admin_login"),
     path('admin_logout/', views.admin_logout, name="admin_logout"),
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
    path('approve_application/<int:id>', views.approve_application, name="approve_application"),
    path('view_users', views.view_users, name="view_users"),
    path('view_recruiters', views.view_recruiters, name="view_recruiters"),
    path('logout/', views.logout, name="logout"),

]