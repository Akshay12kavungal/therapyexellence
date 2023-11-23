from django.contrib import admin
import decimal,csv
from django.http import HttpResponse
#from django.db.models import F

from .models import Therapist_Profile
from .models import Support


# Register your models here.

#@admin.register(MonthlyRegistration)



class Profilesupervisor(admin.ModelAdmin):
	
	list_display=('ID','First_Name','Last_Name','Username','Email','Phone_Number','Password','Confirm_Password','otp','token','uid','joining_date','Age','Gender','Degree','Designation','Address','About','Experience','Specialisation')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	actions=['export_details']

class SupportAdmin(admin.ModelAdmin):
	
	list_display=('Name','Email','Message')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	#list_filter=["Username","Email"]
	actions=['export_details']

admin.site.register(Support,SupportAdmin)
admin.site.register(Therapist_Profile,Profilesupervisor)
