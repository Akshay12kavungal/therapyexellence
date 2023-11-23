from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.crypto import get_random_string
import random



class Admin_Profile(models.Model):

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


class Admin_Invoice(models.Model):
    ID=models.AutoField(primary_key=True,blank=True,unique=True)
    Bill_No=models.CharField(max_length=42)
    Patient_Name=models.CharField(max_length=42)
    Phone_Number=models.CharField(max_length=42)
    Email= models.EmailField()
    Assigned_Therapist= models.CharField(max_length=42)
    Date = models.CharField(max_length=42)
    Address= models.CharField(max_length=42)
    Total_Amount= models.CharField(max_length=42)
    Payment_Method= models.CharField(max_length=42)
    Payment_Status= models.CharField(max_length=42)
    
    
    def __str__(self):
        return self.Bill_No
