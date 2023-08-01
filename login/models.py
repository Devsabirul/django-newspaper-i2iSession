from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    number = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_pic', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
