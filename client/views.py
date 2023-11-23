from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.generic import View
from django.template.loader import get_template
from django.contrib.auth.models import User
from therapyexellence import settings

from .mixins import MessaHandler

import random
from .models import Profile
from .models import Support
from .models import Book_appointments

from django.core.mail import send_mail


from django.core.cache import cache

import smtplib
from django.urls import reverse_lazy




from.helpers import send_forget_password_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from client.models import Book_appointments




#email verification
def send_otp_email(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('login')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Profile.objects.get(Email=Email)
        profile.otp = otp
        profile.save()

        
        subject = 'Your One-Time Password'
        message = f'Your OTP is: {otp}'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'verification.html')
    return render(request, 'send_otp_email.html')





#registration page
def signup(request):

    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('signup')

       

        
        if Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('signup')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('login')





        

        cust_objt=Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password,otp=otp)
        cust_objt.save()
        return render(request,'login.html')
                                
    elif request.method=='GET':
        return render(request,'signup.html')

    else:
         
        return HttpResponse("an expectation occured")

        


#login
def login_with_password(request):
    if request.method=='POST':
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        profile=Profile.objects.filter(Password=Password)
        profile=Profile.objects.filter(Username=Username)
        

        if not profile.exists():
            return redirect('signup')

        return redirect('selectprofile')

       

    return render(request,'login_with_password.html')





def login(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        #Password=request.POST['Password']
        Phone_Number=request.POST.get('Phone_Number')
        profile=Profile.objects.filter(Phone_Number=Phone_Number)
        
        if not profile.exists():
            return redirect('signup')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Profile.objects.get(Phone_Number=Phone_Number)
        profile.otp = otp
        profile.save()
        message_handler=MessaHandler(Phone_Number,profile.otp)
        message_handler.send_otp_on_phone()

    #   return redirect('/otp/{profile[0].uid}')
        return redirect('otp')


            
    return render(request,"login.html")



#otp verfication
def otp(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        profile=Profile.objects.filter(otp=otp)
        if not profile.exists():
            return redirect('signup')

        
           
        return redirect('selectprofile')
       

    return render(request,'verification.html')
#forgetpassword
import uuid
def ForgetPassword(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('login')
        token=str(uuid.uuid4())
        profile = Profile.objects.get(Email=Email)
        profile.token = token
        profile.save()

        
        subject = 'Your One-Time Password'
        message=f'hi,http://127.0.0.1:8000/changepassword'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
       
        return redirect('CheckYourMail')
    return render(request, 'forgetpassword.html')


def CheckYourMail(request):
    if request.method == 'POST':
       
        return redirect('login')  

    return render(request, 'CheckYourMail.html')



#change password
def ChangePassword(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        New_Password=request.POST['New_Password']
        Confirm_Password=request.POST['Confirm_Password']
        
        profile=Profile.objects.filter(Username=Username)
        if not profile.exists():
            return redirect('signup')



        profile = Profile.objects.get(Username=Username)
        profile.Password = New_Password
        profile.Confirm_Password = Confirm_Password

        profile.save()
        
       
        
        
        return redirect('login_with_password')
       

    return render(request,'changepassword.html')


#listing
class CustomerListing(View):
    template_name = 'adusermanagement.html'

    def get(self,request):
        cust_obj = Profile.objects.all()
        context = {
        'adusermanagement':cust_obj
        }
        return render(request,self.template_name,context)

    




    
class clientsuperListing(View):
    template_name = 'superadminuserlist.html'

    def get(self,request):
        cust_obj = Profile.objects.all()
        context = {
        'superadminuserlist':cust_obj
        }
        return render(request,self.template_name,context)


class clientgivesupportListing(View):
    template_name = 'aduserlist.html'

    def get(self,request):
        cust_obj = Profile.objects.all()
        context = {
        'aduserlist':cust_obj
        }
        return render(request,self.template_name,context)

class Book_appointmentsListing(View):
    template_name = 'adupcomingappointment.html'

    def get(self,request):
        cust_obj = Book_appointments.objects.all()
        context = {
        'adupcomingappointment':cust_obj
        }
        return render(request,self.template_name,context)

class upcoming_appointmentsListing(View):
    template_name = 'thupcomingappointment.html'

    def get(self,request):
        cust_obj = Book_appointments.objects.all()
        context = {
        'thupcomingappointment':cust_obj
        }
        return render(request,self.template_name,context)



def logout(request):
    auth.logout(request)
    return render (request,'login.html') 
   

# Create your views here.

def home(request):
    return render(request,"login.html")





#def adminhome(request):
    #return render(request,"adminhome.html")
#def adprofile(request):
    #return render(request,"adprofile.html")

def clienthome(request):
    return render(request,"clienthome.html")

def clienthome(request):
    
   
    thupcomingappointments= Book_appointments.objects.all()

    context = {
        
        'thupcomingappointments': thupcomingappointments,
    }

    template_name = 'clienthome.html'
    return render(request, template_name, context)



def pop_forget(request):
    return render(request,"pop_forget.html")
def pop_signup(request):
    return render(request,"pop_signup.html")

def pop_verification(request):

    return render(request,"pop_verification.html")


def clientprofile(request):
    return render(request,"clientprofile.html")


def clientnotification(request):
    return render(request,"clientnotification.html")
#services

def clientservices(request):
    return render(request,"clientservices.html")

def clientservice1(request):
    return render(request,"clientservice1.html")


def clientservice2(request):
    return render(request,"clientservice2.html")

def clientservice3(request):
    return render(request,"clientservice3.html")



def clientfaq(request):
    return render(request,"clientfaq.html")

def clientsupport(request):
    return render(request,"clientsupport.html")

def clientuserprofile(request):
    return render(request,"clientuserprofile.html")

def selectprofile(request):
    return render(request,"selectprofile.html")
def selectsignupprofile(request):
    return render(request,"selectsignupprofile.html")









def book_appointments(request):
    cust_obj = Book_appointments.objects.all()
    if request.method == 'POST':
        Name=request.POST['Name']
        Problem=request.POST['Problem']
        Date=request.POST['Date']
        Supervisor_Name=request.POST['Supervisor_Name']
        Therapist_Name=request.POST['Therapist_Name']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Age=request.POST['Age']
        Time=request.POST['Time']
        Gender=request.POST['Gender']


       

        cust_obj=Book_appointments(Name=Name,
            Problem=Problem,
            Date=Date,
            Supervisor_Name=Supervisor_Name,
            Therapist_Name=Therapist_Name,
            Email=Email,
            Phone_Number=Phone_Number,
            Age=Age,
            Time=Time,
            Gender=Gender
            )
        cust_obj.save()
        return redirect('clienthome')
    
    return render(request, 'clientbook_appointments.html', {'cust_obj': cust_obj})



def add_clientProfile(request):
    cust_obj = Profile.objects.all()
    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('adusermanagement')

       

        
        if Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('adusermanagement')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('adusermanagement')


        cust_obj=Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password)
        cust_obj.save()
        return redirect('adusermanagement')
    
    return render(request, 'clientaddprofile.html', {'cust_obj': cust_obj})

def delete_Profile(request,ID, *args, **kwargs):
    cust_obj = Profile.objects.get(ID=ID)
    cust_obj.delete()
    return redirect('adusermanagement')

def delete_AllProfile(request):
    cust_obj = Profile.objects.all()
    cust_obj.delete()
    return redirect('adusermanagement')
"""
def Update_Profile(request,ID, *args, **kwargs):
    cust_obj = Profile.objects.get(ID=ID)
    return render(request, 'clientupdateprofile.html', {'cust_obj': cust_obj})
    
"""
#edit profile 
def Update_Profile(request,ID, *args, **kwargs):
    cust_obj = Profile.objects.get(ID=ID)
    if request.method=='GET':
        return render(request, 'clientupdateprofile.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.First_Name=request.POST['First_Name']
        cust_obj.Last_Name=request.POST['Last_Name']
        cust_obj.Username=request.POST['Username']
        cust_obj.Email=request.POST['Email']
        cust_obj.Phone_Number=request.POST['Phone_Number']
        cust_obj.Password=request.POST['Password']
        cust_obj.Confirm_Password=request.POST['Confirm_Password']
        cust_obj.save()
        return redirect('adusermanagement')

 


def clientsupport(request):
    cust_obj = Support.objects.all()

    if request.method == 'POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Message=request.POST['Message']

        cust_obj=Support(Name=Name,Email=Email,Message=Message)
        cust_obj.save()
        return redirect('clienthome')
                                
    elif request.method=='GET':
        return render(request,'clientsupport.html')

    else:
         
        return HttpResponse("an expectation occured")






def delete_appointments(request,Appointment_id, *args, **kwargs):
    cust_obj = Book_appointments.objects.get(Appointment_id=Appointment_id)
    cust_obj.delete()
    return redirect('adupcomingappointment')


#edit profile 
def edit_appointments(request,Appointment_id, *args, **kwargs):
    cust_obj = Book_appointments.objects.get(Appointment_id=Appointment_id)
    if request.method=='GET':
        return render(request, 'clienteditappointments.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.Name=request.POST['Name']
        cust_obj.Email=request.POST['Email']
        cust_obj.Therapist_Name=request.POST['Therapist_Name']
        cust_obj.Date=request.POST['Date']
        cust_obj.save()
        return redirect('adupcomingappointment')


 
def delete_upcoming_appointments(request,Appointment_id, *args, **kwargs):
    cust_obj = Book_appointments.objects.get(Appointment_id=Appointment_id)
    cust_obj.delete()
    return redirect('thupcomingappointment')


#edit profile 
def edit_upcoming_appointments(request,Appointment_id, *args, **kwargs):
    cust_obj = Book_appointments.objects.get(Appointment_id=Appointment_id)
    if request.method=='GET':
        return render(request, 'client_editupcoming_appointments.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.Name=request.POST['Name']
        cust_obj.Email=request.POST['Email']
        cust_obj.Therapist_Name=request.POST['Therapist_Name']
        cust_obj.Date=request.POST['Date']
        cust_obj.save()
        return redirect('thupcomingappointment')

 


def clientviewappointments(request,Appointment_id, *args, **kwargs):
    cust_obj = Book_appointments.objects.get(Appointment_id=Appointment_id)
    if request.method=='GET':
        return render(request, 'clientviewappointments.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.Name=request.POST['Name']
        cust_obj.Email=request.POST['Email']
        cust_obj.Therapist_Name=request.POST['Therapist_Name']
        cust_obj.Date=request.POST['Date']
        cust_obj.save()
        return redirect('adupcomingappointment')