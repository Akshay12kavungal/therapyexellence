from django import forms
from .models import Admin_Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Admin_Profile
        fields = '__all__'