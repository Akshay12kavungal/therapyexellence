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
from .models import Caretaker_Profile

from .mixins import MessaHandler

import random


from django.core.mail import send_mail


from django.core.cache import cache

import smtplib


from django.urls import reverse_lazy
from.helpers import send_forget_password_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




#email verification
def caretakersend_otp_email(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Caretaker_Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('caretakerlogin')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Caretaker_Profile.objects.get(Email=Email)
        profile.otp = otp
        profile.save()

        
        subject = 'Your One-Time Password'
        message = f'Your OTP is: {otp}'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'caretakerverification.html')
    return render(request, 'caretakersend_otp_email.html')





#registration page


def caretakersignup(request):

    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Caretaker_Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('caretakersignup')

       

        
        if Caretaker_Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('caretakersignup')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('caretakerlogin')





        

        cust_objt=Caretaker_Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password)
        cust_objt.save()
        return render(request,'caretakerpop_signup.html')
                                
    elif request.method=='GET':
        return render(request,'caretakersignup.html')

    else:
         
        return HttpResponse("an expectation occured")

        


#login
def caretakerlogin_with_password(request):
    if request.method=='POST':
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        profile=Caretaker_Profile.objects.filter(Password=Password)
        if not profile.exists():
            return redirect('caretakersignup')

        
           
        return redirect('caretakerpop_verification')
       

    return render(request,'caretakerlogin_with_password.html')




#login
def caretakerlogin(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        #Password=request.POST['Password']
        Phone_Number=request.POST.get('Phone_Number')
        profile=Caretaker_Profile.objects.filter(Phone_Number=Phone_Number)
        
        if not profile.exists():
            return redirect('caretakersignup')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Caretaker_Profile.objects.get(Phone_Number=Phone_Number)
        profile.otp = otp
        profile.save()
        message_handler=MessaHandler(Phone_Number,profile.otp)
        message_handler.send_otp_on_phone()

    #   return redirect('/otp/{profile[0].uid}')
        return redirect('caretakerverification')


            
    return render(request,"caretakerlogin.html")



#otp verfication
def caretakerverification(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        profile=Caretaker_Profile.objects.filter(otp=otp)
        if not profile.exists():
            return redirect('caretakersignup')

        
           
        return redirect('caretakerpop_verification')
       

    return render(request,'caretakerverification.html')
#forgetpassword
import uuid
def caretakerForgetPassword(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Caretaker_Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('caretakerlogin')
        token=str(uuid.uuid4())
        profile = Caretaker_Profile.objects.get(Email=Email)
        profile.token = token
        profile.save()

        
        subject = 'Your One-Time Password'
        message=f'hi,http://127.0.0.1:8000/caretakerchangepassword'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Check Your Mail')
    return render(request, 'caretakerforgetpassword.html')






#change password
def caretakerChangePassword(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        New_Password=request.POST['New_Password']
        Confirm_Password=request.POST['Confirm_Password']
        
        profile=Caretaker_Profile.objects.filter(Username=Username)
        if not profile.exists():
            return redirect('caretakersignup')



        profile = Caretaker_Profile.objects.get(Username=Username)
        profile.Password = New_Password
        profile.Confirm_Password = Confirm_Password

        profile.save()
        
       
        
        
        return redirect('caretakerlogin_with_password')
       

    return render(request,'caretakerchangepassword.html')


#listing

class caretakerListing(View):
    template_name = 'adcaretakermanagement.html'

    def get(self,request):
        cust_obj = Caretaker_Profile.objects.all()
        context = {
        'adcaretakermanagement':cust_obj
        }
        return render(request,self.template_name,context)


class caretakersuperListing(View):
    template_name = 'superadmincaretakerlist.html'

    def get(self,request):
        cust_obj = Caretaker_Profile.objects.all()
        context = {
        'superadmincaretakerlist':cust_obj
        }
        return render(request,self.template_name,context)

class caretakergivesupportListing(View):
    template_name = 'adcaretakerlist.html'

    def get(self,request):
        cust_obj = Caretaker_Profile.objects.all()
        context = {
        'adcaretakerlist':cust_obj
        }
        return render(request,self.template_name,context)






   

# Create your views here.

def home(request):
    return render(request,"login.html")


def caretakerpop_forget(request):
    return render(request,"caretakerpop_forget.html")
def caretakerpop_signup(request):
    return render(request,"caretakerpop_signup.html")
def caretakerpop_verification(request):
    return render(request,"caretakerpop_verification.html")


def caretakerhome(request):
    return render(request,"caretakerhome.html")

def caretakerprofile(request):
    return render(request,"caretakerprofile.html")



def logout(request):
    auth.logout(request)
    return render (request,'login.html') 
def add_caretakerProfile(request):
    cust_obj = Caretaker_Profile.objects.all()
    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Caretaker_Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('adcaretakermanagement')

       

        
        if Caretaker_Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('adcaretakermanagement')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('adcaretakermanagement')


        cust_obj=Caretaker_Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password)
        cust_obj.save()
        return redirect('adcaretakermanagement')
    
    return render(request, 'caretakeraddprofile.html', {'cust_obj': cust_obj})



def delete_caretakerProfile(request,ID, *args, **kwargs):
    cust_obj = Caretaker_Profile.objects.get(ID=ID)
    cust_obj.delete()
    return redirect('adcaretakermanagement')

def delete_AllcaretakerProfile(request):
    cust_obj = Caretaker_Profile.objects.all()
    cust_obj.delete()
    return redirect('adcaretakermanagement')
"""
def Update_caretakerProfile(request,ID, *args, **kwargs):
    cust_obj = Caretaker_Profile.objects.get(ID=ID)
    return render(request, 'adminupdateprofile.html', {'cust_obj': cust_obj})
    
"""
#edit profile 
def Update_Profile(request,ID, *args, **kwargs):
    cust_obj = Caretaker_Profile.objects.get(ID=ID)
    if request.method=='GET':
        return render(request, 'caretakerupdateprofile.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.First_Name=request.POST['First_Name']
        cust_obj.Last_Name=request.POST['Last_Name']
        cust_obj.Username=request.POST['Username']
        cust_obj.Email=request.POST['Email']
        cust_obj.Phone_Number=request.POST['Phone_Number']
        cust_obj.Password=request.POST['Password']
        cust_obj.Confirm_Password=request.POST['Confirm_Password']
        cust_obj.save()
        return redirect('adcaretakermanagement')


















