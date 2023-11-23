from django.contrib import admin
from django.urls import path,include
from . import views
from client.views import CustomerListing,clientsuperListing,clientgivesupportListing,Book_appointmentsListing,upcoming_appointmentsListing


from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)



urlpatterns = [
   path('',views.home,name="home"),


   path('signup',views.signup, name="signup"),
   path('login',views.login, name="login"),
   path('login_with_password',views.login_with_password, name="login_with_password"),
   
  
   path('logout',views.logout, name="logout"),
  
   path('selectprofile',views.selectprofile, name="selectprofile"),
   path('selectsignupprofile',views.selectsignupprofile, name="selectsignupprofile"),
   path('home',views.home, name="home"),
   path('verification',views.otp,name="otp"),
   #path('generate_otp',views.generate_otp,name="generate_otp"),
   path('send_otp_email', views.send_otp_email, name='send_otp_email'),
   

   path('forgetpassword', views.ForgetPassword, name='ForgetPassword'),
   path('changepassword', views.ChangePassword, name='changepassword'),
   path('CheckYourMail', views.CheckYourMail, name='CheckYourMail'),



   path(r'adusermanagement',CustomerListing.as_view(),name='adusermanagement'),
   path(r'superadminuserlist',clientsuperListing.as_view(),name='superadminuserlist'),
   path(r'aduserlist',clientgivesupportListing.as_view(),name='aduserlist'),
   path(r'adupcomingappointment',Book_appointmentsListing.as_view(),name='adupcomingappointment'),
   path(r'thupcomingappointment',upcoming_appointmentsListing.as_view(),name='thupcomingappointment'),


   path('clienthome',views.clienthome,name="clienthome"),

   path('pop_forget',views.pop_forget, name="pop_forget"),
   path('pop_signup',views.pop_signup, name="pop_signup"),
   path('pop_verification',views.pop_verification, name="pop_verification"),

   path('clientprofile',views.clientprofile,name="clientprofile"),
   path('clientnotification',views.clientnotification,name="clientnotification"),
   path('clientservices',views.clientservices,name="clientservices"),
   path('clientservice1',views.clientservice1,name="clientservice1"),
   path('clientservice2',views.clientservice2,name="clientservice2"),
   path('clientservice3',views.clientservice3,name="clientservice3"),
   path('clientfaq',views.clientfaq,name="clientfaq"),
   path('clientsupport',views.clientsupport,name="clientsupport"),
   path('clientuserprofile',views.clientuserprofile,name="clientuserprofile"),
   path('clientbook_appointments',views.book_appointments,name="clientbook_appointments"),

   
   path('clientaddprofile', views.add_clientProfile, name='clientaddprofile'),
   #path('admindeleteprofile', views.delete_Profile, name='admindeleteprofile'),
   path('clientdeleteprofile/<int:ID>',views.delete_Profile, name='clientdeleteprofile'),
   path('clientdeleteAllprofile', views.delete_AllProfile, name='clientdeleteAllprofile'),
   path('clientupdateprofile<int:ID>', views.Update_Profile, name='clientupdateprofile'),
   
   path('delete_appointments/<int:Appointment_id>',views.delete_appointments, name='delete_appointments'),
   path('clienteditappointments<int:Appointment_id>', views.edit_appointments, name='clienteditappointments'),

   path('delete_upcoming_appointments/<int:Appointment_id>',views.delete_upcoming_appointments, name='delete_upcoming_appointments'),
   path('client_editupcoming_appointments<int:Appointment_id>', views.edit_upcoming_appointments, name='client_editupcoming_appointments'),

  path('clientviewappointments<int:Appointment_id>', views.clientviewappointments, name='clientviewappointments'),
   
]
   
  
