from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
