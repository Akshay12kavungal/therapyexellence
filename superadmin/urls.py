from django.contrib import admin
from django.urls import path,include
from . import views
from Admin.views import adminListing






urlpatterns = [
   path('',views.home,name="home"),

#  path('services',views.services, name="services"),
  
   path('superadminsignup',views.superadminsignup, name="superadminsignup"),
   path('superadminlogin',views.superadminlogin, name="superadminlogin"),
   path('superadminlogin_with_password',views.superadminlogin_with_password, name='superadminlogin_with_password'),
  
   path('logout',views.logout, name="logout"),
   
  
   path('selectprofile',views.home, name="selectprofile"),
   path('superadminverification',views.superadminverification,name="superadminverification"),
   #path('generate_otp',views.generate_otp,name="generate_otp"),
   path('superadminsend_otp_email', views.superadminsend_otp_email, name='superadminsend_otp_email'),
   

   path('superadminforgetpassword', views.superadminForgetPassword, name='superadminforgetpassword'),
   path('superadminchangepassword', views.superadminChangePassword, name='superadminchangepassword'),


  
   path('superadminhome',views.superadminhome,name="superadminhome"),

   path('superadminpop_forget',views.superadminpop_forget, name="superadminpop_forget"),
   path('superadminpop_signup',views.superadminpop_signup, name="superadminpop_signup"),
   path('superadminpop_verification',views.superadminpop_verification, name="superadminpop_verification"),

   
   
   #path('superadminsupervisorlist',views.superadminsupervisorlist,name="superadminsupervisorlist"),
   #path('superadmintherapistlist',views.superadmintherapistlist,name="superadmintherapistlist"),
   #path('superadmincaretakerlist',views.superadmincaretakerlist,name="superadmincaretakerlist"),
   #path('superadminuserlist',views.superadminuserlist,name="superadminuserlist"),

   #path('superadminadmin',views.superadminadmin,name="superadminadmin"),
   path('superadmintherapistallocator',views.superadmintherapistallocator,name="superadmintherapistallocator"),
   path('superadminservicemanager',views.superadminservicemanager,name="superadminservicemanager"),
   path('superadmininvoice',views.superadmininvoice,name="superadmininvoice"),
   
   
  
  

   
]
   
  
