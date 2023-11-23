from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth.models import User
from therapyexellence import settings
from .models import Superadmin_Profile
from client.models import Profile
from supervisor.models import Supervisor_Profile
from therapist.models import Therapist_Profile
from caretaker.models import Caretaker_Profile


from .mixins import MessaHandler

import random


from django.core.mail import send_mail


from django.core.cache import cache

import smtplib

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

from django.urls import reverse_lazy
from.helpers import send_forget_password_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




#email verification
def superadminsend_otp_email(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Superadmin_Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('superadminlogin')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Superadmin_Profile.objects.get(Email=Email)
        profile.otp = otp
        profile.save()

        
        subject = 'Your One-Time Password'
        message = f'Your OTP is: {otp}'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'superadminverification.html')
    return render(request, 'superadminsend_otp_email.html')





#registration page
def superadminsignup(request):

    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Superadmin_Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('superadminsignup')

       

        
        if Superadmin_Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('superadminsignup')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('superadminlogin')





        

        cust_objt=Superadmin_Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password)
        cust_objt.save()
        return render(request,'superadminpop_signup.html')
                                
    elif request.method=='GET':
        return render(request,'superadminsignup.html')

    else:
         
        return HttpResponse("an expectation occured")

        


#login
def superadminlogin_with_password(request):
    if request.method=='POST':
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        profile=Superadmin_Profile.objects.filter(Password=Password)
        profile=Superadmin_Profile.objects.filter(Username=Username)
        if not profile.exists():
            return redirect('superadminsignup')

        
           
        return redirect('superadminpop_verification')
       

    return render(request,'superadminlogin_with_password.html')




#login
def superadminlogin(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        #Password=request.POST['Password']
        Phone_Number=request.POST.get('Phone_Number')
        profile=Superadmin_Profile.objects.filter(Phone_Number=Phone_Number)
        
        if not profile.exists():
            return redirect('superadminsignup')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Superadmin_Profile.objects.get(Phone_Number=Phone_Number)
        profile.otp = otp
        profile.save()
        message_handler=MessaHandler(Phone_Number,profile.otp)
        message_handler.send_otp_on_phone()

    #   return redirect('/otp/{profile[0].uid}')
        return redirect('superadminverification')


            
    return render(request,"superadminlogin.html")



#otp verfication
def superadminverification(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        profile=Superadmin_Profile.objects.filter(otp=otp)
        if not profile.exists():
            return redirect('superadminsignup')

        
           
        return redirect('superadminpop_verification')
       

    return render(request,'superadminverification.html')
#forgetpassword
import uuid
def superadminForgetPassword(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Superadmin_Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('adminlogin')
        token=str(uuid.uuid4())
        profile = Superadmin_Profile.objects.get(Email=Email)
        profile.token = token
        profile.save()

        
        subject = 'Your One-Time Password'
        message=f'hi,http://127.0.0.1:8000/superadminchangepassword'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Check Your Mail')
    return render(request, 'superadminforgetpassword.html')






#change password
def superadminChangePassword(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        New_Password=request.POST['New_Password']
        Confirm_Password=request.POST['Confirm_Password']
        
        profile=Superadmin_Profile.objects.filter(Username=Username)
        if not profile.exists():
            return redirect('superadminsignup')



        profile = Superadmin_Profile.objects.get(Username=Username)
        profile.Password = New_Password
        profile.Confirm_Password = Confirm_Password

        profile.save()
        
       
        
        
        return redirect('superadminlogin_with_password')
       

    return render(request,'superadminchangepassword.html')


def superadminpop_forget(request):
    return render(request,"superadminpop_forget.html")
def superadminpop_signup(request):
    return render(request,"superadminpop_signup.html")
def superadminpop_verification(request):
    return render(request,"superadminpop_verification.html")




#main view

def home(request):
    return render(request,"selectprofile.html")



"""
def superadminhome(request):
    return render(request,"superadminhome.html")
"""
#activity
def superadmincaretakerlist(request):
    return render(request,"superadmincaretakerlist.html")

def superadminsupervisorlist(request):
    return render(request,"superadminsupervisorlist.html")

def superadmintherapistlist(request):
    return render(request,"superadmintherapistlist.html")

def superadminuserlist(request):
    return render(request,"superadminuserlist.html")

#Admin list

def superadminadmin(request):
    return render(request,"superadminadmin.html")

#systems

def superadmintherapistallocator(request):
    return render(request,"superadmintherapistallocator.html")

def superadminservicemanager(request):
    return render(request,"superadminservicemanager.html")



def superadmininvoice(request):
    return render(request,"superadmininvoice.html")


def superadminhome(request):
    client_count = Profile.objects.all().count()
    caretaker_count = Caretaker_Profile.objects.all().count()
    supervisor_count = Supervisor_Profile.objects.all().count()
    therapist_count = Therapist_Profile.objects.all().count()


   
    
    return render(request, 'superadminhome.html', {
        'client_count': client_count,
        'caretaker_count': caretaker_count,
        'supervisor_count': supervisor_count,
        'therapist_count': therapist_count,
        
    })












def logout(request):
    
    messages.success(request,"logged out sucessfuly")
    return redirect('adminlogin')

























