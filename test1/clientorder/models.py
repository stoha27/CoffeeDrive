from django.db import models
from test.regrtest import DESCRIPTION
from django.utils.translation import ugettext_lazy as _

class Client(models.Model):
    name = models.CharField(max_length=120, verbose_name = _('name of client'))
    nick_name = models.CharField(max_length=120, verbose_name = _('nickname'))
    email = models.EmailField(max_length=120, verbose_name = _('mail of client'))
    telephone = models.CharField(max_length=120, verbose_name =_('telephone number'))
#   bank_account =  models.CharField(max_length=120)

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')

class Goods (models.Model):
    name=models.CharField(max_length=120, verbose_name = _('name of good'))
    price=models.IntegerField(verbose_name = _('value'))


    class Meta:
         verbose_name = 'Coffee goods'
     
 
class Order (models.Model):
    count=models.IntegerField(verbose_name = _('counter'))
    name_Goods=models.ManyToManyField(Goods, verbose_name = _('name of good'))
    date_of_order = models.DateTimeField(verbose_name = _('date of order'))
    date_of_accept = models.DateTimeField(verbose_name = _('date of orders accept'))
    date_prognosis_act = models.DateTimeField(verbose_name = _('prognosis date of sale action'))
    date_fact_act = models.DateTimeField(verbose_name = _('actual date of sale action'))


    class Meta:
         verbose_name = 'order'


class UserProfile (models.Model):
    name_of_cafe=models.CharField(max_length=120)
    description=models.TextField()
        
    
class GroupOrder (models.Model):
    client=models.ForeignKey(Client)
    cafe=models.ForeignKey(UserProfile)
    order=models.ManyToManyField(Order)    


class User(models.Model):
    fname = models.CharField(max_length=50, verbose_name = _('first name'))

    class Meta:
         verbose_name = "users"
    
#class Order (models.Model):
#    name_of_cafe = models.CharField(max_length=120) 
#    description_of_cafe = models.TextField()
#    name = models.ManyToManyField (Goods)
#   size_of_good = models.ManyToManyField (Goods)
#    take_with_you = models.BooleanField()
# ChoiceField
#    to_reserve_table =models.BooleanField()
#ChoiceField
    

#class OrderGroup (models.Model):
#    order=models.ManyToMany(Order)
#    count=models.IntegerField()
#count=models.ManyToMany(Clients)
