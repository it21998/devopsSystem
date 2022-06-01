"""student_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student_management import settings
from django.conf.urls.static import static
from student_management_app import views
from student_management_app import views,StaffViews, StudentViews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('doLogin',views.doLogin,name="do_login"),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
   
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('student_home', StudentViews.student_home, name="student_home"),
    path('manage_applications', StudentViews.manage_applications,name="manage_applications"),
    path('add_application',StudentViews.add_application,name="add_application"),
    path('staff_manage_applications', StaffViews.staff_manage_applications,name="staff_manage_applications"),
    path('edit_application/<str:application_id>', StaffViews.edit_application,name="edit_application"),
    path('edit_application_save', StaffViews.edit_application_save,name="edit_application_save"),
    path('add_application_save',StudentViews.add_application_save,name="add_application_save"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
