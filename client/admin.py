from django.contrib import admin
import decimal,csv
from django.http import HttpResponse
#from django.db.models import F

from .models import Profile
from .models import Support
from .models import Book_appointments


# Register your models here.

#@admin.register(MonthlyRegistration)



class ProfileClient(admin.ModelAdmin):
	
	list_display=('ID','First_Name','Last_Name','Username','Email','Phone_Number','Password','Confirm_Password','otp','token','uid')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	actions=['export_details']

class SupportAdmin(admin.ModelAdmin):
	
	list_display=('Name','Email','Message')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	#list_filter=["Username","Email"]
	actions=['export_details']
class Book_appointmentsAdmin(admin.ModelAdmin):
	
	list_display=('Appointment_id','Name','Problem','Date','Supervisor_Name','Therapist_Name','Email','Phone_Number','Age','Time','Gender')
	#search_fields=CustomerDetail.SearchableFields
	
	list_per_page=4
	#list_filter=["Username","Email"]
	actions=['export_details']



admin.site.register(Book_appointments,Book_appointmentsAdmin)

admin.site.register(Support,SupportAdmin)

admin.site.register(Profile,ProfileClient)

