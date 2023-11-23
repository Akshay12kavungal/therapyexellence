from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.crypto import get_random_string
import random



class Profile(models.Model):

    ID=models.AutoField(primary_key=True,blank=True,unique=True)
    First_Name=models.CharField(max_length=42)
    Last_Name=models.CharField(max_length=42)
    Username= models.CharField(max_length=42)
    Email= models.EmailField()
    Phone_Number=models.IntegerField(default=0)
    Password= models.CharField(max_length=42)
    Confirm_Password= models.CharField(max_length=42)
    otp=models.CharField(max_length=6, blank=True, null=True,editable=False)
    token=models.CharField(max_length=10,blank=True,null=True,editable=True)

    uid = models.CharField(max_length=4, unique=True, editable=False)
    joining_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # generate a unique uid for the new instance
            self.uid = get_random_string(length=4)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.Username

        
class Support(models.Model):
    Name=models.CharField(max_length=42)
    Email= models.EmailField()
    Message= models.CharField(max_length=42)

    def __str__(self):
        return self.Name
class Book_appointments(models.Model):
    
    Appointment_id=models.AutoField(primary_key=True,blank=True,unique=True)
    Name=models.CharField(max_length=42)
    Date=models.CharField(max_length=42)
    Problem=models.CharField(max_length=42)
    Supervisor_Name=models.CharField(max_length=42)
    Therapist_Name=models.CharField(max_length=42)
    Email= models.EmailField()
    Phone_Number=models.CharField(max_length=42)
    Age=models.CharField(max_length=3)
    Time=models.CharField(max_length=42)
    Gender=models.CharField(max_length=42)
    

    


    def __str__(self):
        return self.Name
