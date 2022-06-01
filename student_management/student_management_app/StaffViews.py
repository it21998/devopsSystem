from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from student_management_app.models import Aithsh, CustomUser, Students
from django.core.mail import send_mail


def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")


def staff_manage_applications(request):
    applications=Aithsh.objects.filter(status="pending")
    return render(request,"staff_template/staff_manage_applications.html",{"applications":applications})


def edit_application(request,application_id):
    applications=Aithsh.objects.get(id=application_id)
    return render(request,"staff_template/edit_application_template.html",{"applications":applications,"id":application_id})

def edit_application_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        application_id=request.POST.get("application_id")
        try:
            application=Aithsh.objects.get(id=application_id)
            
            stu_id=CustomUser.objects.get(id=application.student_id.admin_id)
            application.status=request.POST.get("status")
            application.save()
            send_mail(
                'Application Status changed',
                "Your application's status has changed!Your ID:"+str(application.student_id.id)+" Username: "+str(stu_id.username),
                request.user.email,
                [stu_id.email],
                fail_silently=False,)
            messages.success(request,"Successfully Edited Application")
            return HttpResponseRedirect(reverse("edit_application",kwargs={"application_id":application_id}))
        except:
            messages.error(request,"Failed to Edit Application")
            return HttpResponseRedirect(reverse("edit_application",kwargs={"application_id":application_id}))

