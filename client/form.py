from django import forms 
from .models import UserProfile

class UserProfileForm(forms.ModelForm): 
    class Meta: 
        model = UserProfile 
        fields = ['user', 'profile_picture','biography','contact_info'] 