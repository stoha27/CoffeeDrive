from django.contrib import admin
from clientorder.models import Client, Goods, Order, UserProfile, GroupOrder




# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    field = ['count', 'name_Goods', 'date_of_order']
    
admin.site.register(Goods)
admin.site.register(Client)

admin.site.register(Order, OrderAdmin) 


 





  
