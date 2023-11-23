from django.contrib import admin
import decimal,csv
from django.http import HttpResponse
#from django.db.models import F

from .models import Admin_Profile
from .models import Support
from .models import Admin_Invoice




# Register your models here.

#@admin.register(MonthlyRegistration)



class Admin_ProfileAdmin(admin.ModelAdmin):
	
	list_display=('ID','First_Name','Last_Name','Username','Email','Phone_Number','Password','Confirm_Password','otp','token','uid','joining_date')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	list_filter=["Username","Email"]
	actions=['export_details']

class SupportAdmin(admin.ModelAdmin):
	
	list_display=('Name','Email','Message')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	#list_filter=["Username","Email"]
	actions=['export_details']


class Admin_Invoice_admin(admin.ModelAdmin):
	
	list_display=('ID','Bill_No','Patient_Name','Phone_Number','Email','Assigned_Therapist','Date','Address','Total_Amount','Payment_Method','Payment_Status')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	#list_filter=["Username","Email"]
	actions=['export_details']

admin.site.register(Admin_Profile,Admin_ProfileAdmin)
admin.site.register(Support,SupportAdmin)
admin.site.register(Admin_Invoice,Admin_Invoice_admin)