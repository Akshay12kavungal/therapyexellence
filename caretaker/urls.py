from django.contrib import admin
from django.urls import path,include
from . import views
from caretaker.views import caretakerListing,caretakersuperListing,caretakergivesupportListing
 
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)







urlpatterns = [
   path('',views.home,name="home"),

#  path('services',views.services, name="services"),
  
   path('caretakersignup',views.caretakersignup, name="caretakercaretakersignup"),
   path('caretakerlogin',views.caretakerlogin, name="caretakerlogin"),
   path('caretakerlogin_with_password',views.caretakerlogin_with_password, name='caretakerlogin_with_password'), 
   path('logout',views.logout, name="logout"),
   path(r'adcaretakermanagement',caretakerListing.as_view(),name='adcaretakermanagement'), 
   path(r'superadmincaretakerlist',caretakersuperListing.as_view(),name='superadmincaretakerlist'),
   path(r'adcaretakerlist',caretakergivesupportListing.as_view(),name='adcaretakerlist'), 
 


   path('selectprofile',views.home, name="selectprofile"),
   path('caretakerverification',views.caretakerverification,name="caretakerverification"),
   #path('generate_otp',views.generate_otp,name="generate_otp"),
   path('caretakersend_otp_email', views.caretakersend_otp_email, name='caretakersend_otp_email'),
   path('caretakerforgetpassword', views.caretakerForgetPassword, name='caretakerforgetpassword'),
   path('caretakerchangepassword', views.caretakerChangePassword, name='caretakerchangepassword'),  
   path('caretakerpop_forget',views.caretakerpop_forget, name="caretakerpop_forget"),
   path('caretakerpop_signup',views.caretakerpop_signup, name="caretakerpop_signup"),
   path('caretakerpop_verification',views.caretakerpop_verification, name="caretakerpop_verification"),

   path('caretakerhome',views.caretakerhome,name="caretakerhome"),
   path('caretakerprofile',views.caretakerprofile,name="caretakerprofile"),

   path('caretakerdeleteprofile/<int:ID>',views.delete_caretakerProfile,name="caretakerprofile"),
   path('caretakerdeleteAllprofile',views.delete_AllcaretakerProfile,name="caretakerdeleteAllprofile"),
   path('caretakerupdateprofile<int:ID>',views.Update_Profile,name="caretakerupdateprofile"),

   path('caretakeraddprofile', views.add_caretakerProfile, name='caretakeraddprofile'),
   
  

   
]
   
  
