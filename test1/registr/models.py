from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class UserProfile(AbstractUser):
    shopName = models.CharField(max_length=30, blank=True, verbose_name=_('Name of Shop'))
    geoPosition = models.CharField(max_length=244, null=True, verbose_name=_('Location'))
    emails = models.EmailField(max_length=244, verbose_name=_('Emails'))
    telWork = models.CharField(max_length=20, null=True, verbose_name=_('Tel work'))
    telMobile = models.CharField(max_length=20, null=True, verbose_name=_('Tel mobile'))
    skype = models.CharField(max_length=244, blank=True, verbose_name=_('Skype'))
    adress = models.CharField(max_length=244, blank=True, verbose_name=_('Adress'))
    contact = models.CharField(max_length=244, blank=True, verbose_name=_('Contacts'))

    def __str__(self):
        return self.shopName + ' - ' + self.adress