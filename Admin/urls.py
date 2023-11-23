from django.contrib import admin
from django.urls import path,include
from . import views
from Admin.views import adminListing
from Admin.views import AdminInvoiceListing,homeInvoiceListing








urlpatterns = [
   path('',views.home,name="home"),

#  path('services',views.services, name="services"),
  
   path('adminsignup',views.adminsignup, name="adminsignup"),
   path('adminlogin',views.adminlogin, name="adminlogin"),
   path('adminlogin_with_password',views.adminlogin_with_password, name='adminlogin_with_password'),
  
   path('logout',views.logout, name="logout"),
   path(r'superadminadmin',adminListing.as_view(),name='superadminadmin'),

  
   path('selectprofile',views.home, name="selectprofile"),
   path('adminverification',views.adminverification,name="adminverification"),
   #path('generate_otp',views.generate_otp,name="generate_otp"),
   path('adminsend_otp_email', views.adminsend_otp_email, name='adminsend_otp_email'),
   

   path('adminforgetpassword', views.adminForgetPassword, name='adminforgetpassword'),
   path('adminchangepassword', views.adminChangePassword, name='adminchangepassword'),


  
   path('adminhome',views.adminhome,name="adminhome"),

   path('adminpop_forget',views.adminpop_forget, name="adminpop_forget"),
   path('adminpop_signup',views.adminpop_signup, name="adminpop_signup"),
   path('adminpop_verification',views.adminpop_verification, name="adminpop_verification"),

   path('adprofile',views.adprofile,name="adprofile"),
   path('adnotification',views.adnotification,name="adnotification"),

   #path('adupcomingappointment',views.adupcomingappointment,name="adupcomingappointment"),

   path('adpastappointment',views.adpastappointment,name="adpastappointment"),

   #path('adsupervisorlist',views.adsupervisorlist,name="adsupervisorlist"),
   #path('adtherapistlist',views.adtherapistlist,name="adtherapistlist"),
   #path('adcaretakerlist',views.adcaretakerlist,name="adcaretakerlist"),
   #path('aduserlist',views.aduserlist,name="aduserlist"),

   #path('adsupervisormanagement',views.adsupervisormanagement,name="adsupervisormanagement"),
   #path('adtherapistmanagement',views.adtherapistmanagement,name="adtherapistmanagement"),
   #path('adcaretakermanagement',views.adcaretakermanagement,name="adcaretakermanagement"),
   #path('adusermanagement',views.adusermanagement,name="adusermanagement"),
   path('adfaq',views.adfaq,name="adfaq"),
   path('adsupport',views.adsupport,name="adsupport"),
   #path('adinvoice',views.adinvoice,name="adinvoice"),

   path(r'adinvoice',AdminInvoiceListing.as_view(),name='adinvoice'),
  

   path('adminaddinvoice',views.adminaddinvoice,name="adminaddinvoice"),
   path('adrewardsystem',views.adrewardsystem,name="adrewardsystem"),




   path('adminaddprofile', views.add_Profile, name='adminaddprofile'),
   #path('admindeleteprofile', views.delete_Profile, name='admindeleteprofile'),
   path('admindeleteprofile/<int:ID>',views.delete_Profile, name='admindeleteprofile'),
   path('admindeleteAllprofile', views.delete_AllProfile, name='admindeleteAllprofile'),
   path('adminupdateprofile<int:ID>', views.Update_Profile, name='adminupdateprofile'),
   path('Adminupdateinvoice<int:ID>', views.Update_invoice, name='Adminupdateinvoice'),

   path('export-invoices', views.export_invoices, name='export_invoices'),

 

  
  
   
]
   
  
