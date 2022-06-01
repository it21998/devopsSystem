from contextlib import nullcontext
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from pkg_resources import require
from student_management_app.models import Aithsh, Students
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

def student_home(request):
    return render(request,"student_template/student_home_template.html")


def add_application(request):
        return render(request,"student_template/student_add_application_template.html")


def add_application_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        studies=request.POST.get("studies")
        experience=request.POST.get("experience")
        scholarships=request.POST.get("scholarships")
        communication=request.POST.get("communication")
        student_id=request.user.students.id
        student_id=Students.objects.get(id=student_id)
        status="pending"

        try:
            application=Aithsh(studies=studies,experience=experience,scholarships=scholarships,communication=communication,student_id=student_id,status=status)
            application.save()
            send_mail(
                'New Application Created ',
                "New application created by ID: "+str(request.user.students.id)+" Username: "+str(request.user.username),
                request.user.email,
                ['grammateia@hua.gr'],
                fail_silently=False,)
            messages.success(request,"Successfully Added Application")
            return HttpResponseRedirect(reverse("add_application"))
        except:
            messages.error(request,"Failed to Add Application")
            return HttpResponseRedirect(reverse("add_application"))



def manage_applications(request):
    applications=Aithsh.objects.all()
    return render(request,"student_template/student_manage_applications_template.html",{"applications":applications})
