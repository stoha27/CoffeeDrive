from django.db import models
from test.regrtest import DESCRIPTION
#from goods.models import Goods


class Client(models.Model):
    name = models.CharField(max_length=120)
    nick_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    telephone = models.CharField(max_length=120)
#   bank_account =  models.CharField(max_length=120)

    class Meta:
        verbose_name = 'клиент'


class Goods (models.Model):
    name=models.CharField(max_length=120)
    price=models.IntegerField()


    class Meta:
         verbose_name = 'кофейные_штучки'
     
 
class Order (models.Model):
    count=models.IntegerField()
    name_Goods=models.ManyToManyField(Goods)
    date_of_order = models.DateTimeField()
    date_of_accept = models.DateTimeField()
    date_prognosis_act = models.DateTimeField()
    date_fact_act = models.DateTimeField()


    class Meta:
         verbose_name = 'заказ'


class UserProfile (models.Model):
    name_of_cafe=models.CharField(max_length=120)
    description=models.TextField()
        
    
class GroupOrder (models.Model):
    client=models.ForeignKey(Client)
    cafe=models.ForeignKey(UserProfile)
    order=models.ManyToManyField(Order)    


class User(models.Model):
    fname = models.CharField(max_length=50, verbose_name = 'first name')

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
