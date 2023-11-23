from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from .models import Profile

@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()