from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    shopName = models.CharField(max_length=30, blank=True)
    geoPosition = models.CharField(max_length=244, null=True)
    emails = models.EmailField(max_length=244)
    telWork = models.CharField(max_length=20, null=True)
    telMobile = models.CharField(max_length=20, null=True)
    skype = models.CharField(max_length=244, blank=True)
    adress = models.CharField(max_length=244, blank=True)
    contact = models.CharField(max_length=244, blank=True)