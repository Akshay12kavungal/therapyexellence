from django.contrib import admin
import decimal,csv
from django.http import HttpResponse
#from django.db.models import F

from .models import Superadmin_Profile


# Register your models here.

#@admin.register(MonthlyRegistration)



class ProfileSuperadmin(admin.ModelAdmin):
	
	list_display=('ID','First_Name','Last_Name','Username','Email','Phone_Number','Password','Confirm_Password','otp','token','uid','joining_date')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	actions=['export_details']


admin.site.register(Superadmin_Profile,ProfileSuperadmin)
