from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, ClientProfile
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        ClientProfile.objects.create(user=instance, status='C')
    elif created and instance.is_superuser:
        Profile.objects.create(user=instance, status='A')
    elif created and instance.is_staff:
        Profile.objects.create(user=instance, status='M')

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()