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
from .models import Admin_Profile
from .models import Admin_Invoice


from client.models import Profile
from supervisor.models import Supervisor_Profile
from therapist.models import Therapist_Profile
from caretaker.models import Caretaker_Profile
from client.models import Book_appointments
import csv
from openpyxl import Workbook
from reportlab.pdfgen import canvas





from .models import Support
from .forms import ProfileForm

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
def adminsend_otp_email(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Admin_Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('adminlogin')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Admin_Profile.objects.get(Email=Email)
        profile.otp = otp
        profile.save()

        
        subject = 'Your One-Time Password'
        message = f'Your OTP is: {otp}'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'adminverification.html')
    return render(request, 'adminsend_otp_email.html')





#registration page
def adminsignup(request):

    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Admin_Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('adminsignup')

       
        if Admin_Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('adminsignup')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('adminlogin')


        cust_objt=Admin_Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password)
        cust_objt.save()
        return render(request,'adminpop_signup.html')
                                
    elif request.method=='GET':
        return render(request,'adminsignup.html')

    else:
         
        return HttpResponse("an expectation occured")

        


#login
def adminlogin_with_password(request):
    if request.method=='POST':
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        profile=Admin_Profile.objects.filter(Password=Password)
        profile=Admin_Profile.objects.filter(Username=Username)
        if not profile.exists():
            return redirect('adminsignup')

        
           
        return redirect('adminpop_verification')
       

    return render(request,'adminlogin_with_password.html')




#login
def adminlogin(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        #Password=request.POST['Password']
        Phone_Number=request.POST.get('Phone_Number')
        profile=Admin_Profile.objects.filter(Phone_Number=Phone_Number)
        
        if not profile.exists():
            return redirect('adminsignup')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        profile = Admin_Profile.objects.get(Phone_Number=Phone_Number)
        profile.otp = otp
        profile.save()
        message_handler=MessaHandler(Phone_Number,profile.otp)
        message_handler.send_otp_on_phone()

    #   return redirect('/otp/{profile[0].uid}')
        return redirect('adminverification')


            
    return render(request,"adminlogin.html")



#otp verfication
def adminverification(request):
    if request.method=='POST':
        otp=request.POST.get('otp')
        profile=Admin_Profile.objects.filter(otp=otp)
        if not profile.exists():
            return redirect('adminsignup')

        
           
        return redirect('adminpop_verification')
       

    return render(request,'adminverification.html')
#forgetpassword
import uuid
def adminForgetPassword(request):
    if request.method == 'POST':
        Email=request.POST.get('Email')
        profile=Admin_Profile.objects.filter(Email=Email)
        if not profile.exists():
            return redirect('adminlogin')
        token=str(uuid.uuid4())
        profile = Admin_Profile.objects.get(Email=Email)
        profile.token = token
        profile.save()

        
        subject = 'Your One-Time Password'
        message=f'hi,http://127.0.0.1:8000/adminchangepassword'
        from_email = 'akshayaakk90@gmail.com'
        recipient_list = [Email]
        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Check Your Mail')
    return render(request, 'adminforgetpassword.html')






#change password
def adminChangePassword(request):
    if request.method == 'POST':
        Username=request.POST.get('Username')
        New_Password=request.POST['New_Password']
        Confirm_Password=request.POST['Confirm_Password']
        
        profile=Admin_Profile.objects.filter(Username=Username)
        if not profile.exists():
            return redirect('adminsignup')



        profile = Admin_Profile.objects.get(Username=Username)
        profile.Password = New_Password
        profile.Confirm_Password = Confirm_Password

        profile.save()
        
       
        
        
        return redirect('adminlogin_with_password')
       

    return render(request,'adminchangepassword.html')


#listing
class adminListing(View):
    template_name = 'superadminadmin.html'

    def get(self,request):
        cust_obj = Admin_Profile.objects.all()
        context = {
        'superadminadmin':cust_obj
        }
        return render(request,self.template_name,context)

    






def logout(request):
    auth.logout(request)
    return render (request,'login.html') 

# Create your views here.

def home(request):
    return render(request,"login.html")


def adminpop_forget(request):
    return render(request,"adminpop_forget.html")
def adminpop_signup(request):
    return render(request,"adminpop_signup.html")
def adminpop_verification(request):
    return render(request,"adminpop_verification.html")

def adminhome(request):
    return render(request,"adminhome.html")


def adprofile(request):
    return render(request,"adprofile.html")


def adnotification(request):
    return render(request,"adnotification.html")
#manage appointments

#def adupcomingappointment(request):
#    return render(request,"adupcomingappointment.html")

def adpastappointment(request):
    return render(request,"adpastappointment.html")
#give support

#def adsupervisorlist(request):
#    return render(request,"adsupervisorlist.html")

#def adtherapistlist(request):
#    return render(request,"adtherapistlist.html")

#def adcaretakerlist(request):
#    return render(request,"adcaretakerlist.html")

#def aduserlist(request):
#    return render(request,"aduserlist.html")

#user management
def adsupervisormanagement(request):
    return render(request,"adsupervisormanagement.html")

def adtherapistmanagement(request):
    return render(request,"adtherapistmanagement.html")

def adcaretakermanagement(request):
    return render(request,"adcaretakermanagement.html")

def adusermanagement(request):
    return render(request,"adusermanagement.html")

def adrewardsystem(request):
    return render(request,"adrewardsystem.html")



class AdminInvoiceListing(View):
    template_name = 'adinvoice.html'

    def get(self,request):
        cust_obj = Admin_Invoice.objects.all()
        context = {
        'adinvoice':cust_obj
        }
        return render(request,self.template_name,context)

    
class homeInvoiceListing(View):
    template_name = 'adminhome.html'

    def get(self,request):
        cust_obj = Admin_Invoice.objects.all()
        context = {
        'adminhome':cust_obj
        }
        return render(request,self.template_name,context)


def adminaddinvoice(request):

    if request.method == 'POST':
        Bill_No=request.POST['Bill_No']
        Patient_Name=request.POST['Patient_Name']
        Phone_Number=request.POST['Phone_Number']
        Email=request.POST['Email']
        Assigned_Therapist=request.POST['Assigned_Therapist']
        Date=request.POST['Date']
        Address=request.POST['Address']
        Total_Amount=request.POST['Total_Amount']
        Payment_Method=request.POST['Payment_Method']
        Payment_Status=request.POST['Payment_Status']

        if Admin_Invoice.objects.filter(Bill_No=Bill_No):
           return redirect('adminaddinvoice')

        if not Bill_No.isdigit():
            messages.error(request,"Bill No must be digit")
            return redirect('adinvoice')


      
       

        cust_objt=Admin_Invoice(Bill_No=Bill_No,Patient_Name=Patient_Name,Phone_Number=Phone_Number,Email=Email,Assigned_Therapist=Assigned_Therapist,Date=Date,Address=Address,Total_Amount=Total_Amount,Payment_Method=Payment_Method,Payment_Status=Payment_Status)
        cust_objt.save()
        return redirect('adinvoice')
                                

                                
    elif request.method=='GET':
        return render(request,'adminaddinvoice.html')

    else:
         
        return HttpResponse("an expectation occured")




def adfaq(request):
    return render(request,"adfaq.html")



def add_Profile(request):
    cust_obj = Admin_Profile.objects.all()
    if request.method == 'POST':
        First_Name=request.POST['First_Name']
        Last_Name=request.POST['Last_Name']
        Username=request.POST['Username']
        Email=request.POST['Email']
        Phone_Number=request.POST['Phone_Number']
        Password=request.POST['Password']
        Confirm_Password=request.POST['Confirm_Password']

        if Admin_Profile.objects.filter(Username=Username):
           messages.error(request,"Username already exist")
           return redirect('superadminadmin')

       

        
        if Admin_Profile.objects.filter(Email=Email):
            messages.error(request,"email already registered")
            return redirect('superadminadmin')

        if len(Username)>10:
            messages.error(request,"user name must be under 10 characters")

        if Password!=Confirm_Password:
            messages.error(request,"password didn't match")

        if not Username.isalnum():
            messages.error(request,"Username must be alpha-numeric")
            return redirect('superadminadmin')






        cust_obj=Admin_Profile(First_Name=First_Name,Last_Name=Last_Name,Username=Username,Email=Email,Phone_Number=Phone_Number,Password=Password,Confirm_Password=Confirm_Password)
        cust_obj.save()
        return redirect('superadminadmin')
    
    return render(request, 'adminaddprofile.html', {'cust_obj': cust_obj})


def delete_Profile(request,ID, *args, **kwargs):
    cust_obj = Admin_Profile.objects.get(ID=ID)
    cust_obj.delete()
    return redirect('superadminadmin')

def delete_AllProfile(request):
    cust_obj = Admin_Profile.objects.all()
    cust_obj.delete()
    return redirect('superadminadmin')
"""
def Update_Profile(request,ID, *args, **kwargs):
    cust_obj = Profile.objects.get(ID=ID)
    cust_item= Profile.objects.all()
    context={
            'cust_obj':cust_item,
            'cust_item':cust_item
    }
    return render(request, 'adminupdateprofile.html',context)
"""    
#edit profile 
def Update_Profile(request,ID, *args, **kwargs):
    cust_obj = Admin_Profile.objects.get(ID=ID)
    if request.method=='GET':
        return render(request, 'adminupdateprofile.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.First_Name=request.POST['First_Name']
        cust_obj.Last_Name=request.POST['Last_Name']
        cust_obj.Username=request.POST['Username']
        cust_obj.Email=request.POST['Email']
        cust_obj.Phone_Number=request.POST['Phone_Number']
        cust_obj.Password=request.POST['Password']
        cust_obj.Confirm_Password=request.POST['Confirm_Password']
        cust_obj.save()
        return redirect('superadminadmin')




def adsupport(request):
    cust_obj = Support.objects.all()

    if request.method == 'POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Message=request.POST['Message']

        cust_obj=Support(Name=Name,Email=Email,Message=Message)
        cust_obj.save()
        return redirect('adminhome')
                                
    elif request.method=='GET':
        return render(request,'adsupport.html')

    else:
         
        return HttpResponse("an expectation occured")

        

def adminhome(request):
    client_count = Profile.objects.all().count()
    caretaker_count = Caretaker_Profile.objects.all().count()
    supervisor_count = Supervisor_Profile.objects.all().count()
    therapist_count = Therapist_Profile.objects.all().count()
    client_appointments = Book_appointments.objects.all().count()
    invoices = Admin_Invoice.objects.all()

    context = {
        'client_count': client_count,
        'caretaker_count': caretaker_count,
        'supervisor_count': supervisor_count,
        'therapist_count': therapist_count,
        'client_appointments': client_appointments,
        'invoices': invoices,
    }

    template_name = 'adminhome.html'
    return render(request, template_name, context)


def Update_invoice(request,ID, *args, **kwargs):
    cust_obj = Admin_Invoice.objects.get(ID=ID)
    if request.method=='GET':
        return render(request, 'Adminupdateinvoice.html', {'cust_obj': cust_obj})
    if request.method=='POST':
        cust_obj.Bill_No=request.POST['Bill_No']
        cust_obj.Patient_Name=request.POST['Patient_Name']
        cust_obj.Phone_Number=request.POST['Phone_Number']
        cust_obj.Email=request.POST['Email']
        cust_obj.Assigned_Therapist=request.POST['Assigned_Therapist']
        cust_obj.Date=request.POST['Date']
        cust_obj.Address=request.POST['Address']
        cust_obj.Total_Amount=request.POST['Total_Amount']
        cust_obj.Payment_Method=request.POST['Payment_Method']
        cust_obj.Payment_Status=request.POST['Payment_Status']

        cust_obj.save()
        return redirect('adinvoice')




"""
download for csv file

def export_invoices(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="invoices.csv"'

    # Write CSV data to the response
    writer = csv.writer(response)
    writer.writerow(['Bill No', 'Date', 'Patient', 'Therapist', 'Charges', 'Tax', 'Discount', 'Total'])

    # Retrieve invoice data from your database or source
    invoices = Admin_Invoice.objects.all()


    # Write invoice data to CSV rows
    for invoice in invoices:
        writer.writerow([
            invoice.Bill_No,
            invoice.Date,
            invoice.Patient_Name,
            invoice.Assigned_Therapist,
            invoice.Total_Amount


        ])

    return response

"""


"""

export as xlsx formate
def export_invoices(request):
    # Create a new Excel workbook and select the active sheet
    workbook = Workbook()
    sheet = workbook.active

    # Set the column headers
    sheet.append(['Bill No', 'Date', 'Patient', 'Therapist','Total'])

    # Retrieve invoice data from your database or source
    invoices = Admin_Invoice.objects.all()

    # Write invoice data to the Excel sheet
    for invoice in invoices:
        sheet.append([
            invoice.Bill_No,
            invoice.Date,
            invoice.Patient_Name,
            invoice.Assigned_Therapist,
            invoice.Total_Amount
        ])

    # Create a response with the Excel file content type and headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=invoices.xlsx'

    # Save the Excel workbook to the response
    workbook.save(response)

    return response

"""

def export_invoices(request):
    # Create a new PDF canvas
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=invoices.pdf'
    p = canvas.Canvas(response)

    # Retrieve invoice data from your database or source
    invoices = Admin_Invoice.objects.all()

    # Set the font and font size
    p.setFont('Helvetica', 12)

    # Set the column headers
    headers = ['Bill No', 'Date', 'Patient', 'Therapist','Total']
    row_height = 20
    column_width = 100
    x = 40
    y = 750
    for header in headers:
        p.drawString(x, y, header)
        x += column_width

    # Write invoice data to the PDF file
    x = 40
    y -= row_height
    for invoice in invoices:
        p.drawString(x, y, str(invoice.Bill_No))
        x += column_width
        p.drawString(x, y, str(invoice.Date))
        x += column_width
        p.drawString(x, y, invoice.Patient_Name)
        x += column_width
        p.drawString(x, y, invoice.Assigned_Therapist)
        x += column_width
        p.drawString(x, y, str(invoice.Total_Amount))
        x = 40
        y -= row_height

    # Save the PDF canvas
    p.showPage()
    p.save()

    return response

