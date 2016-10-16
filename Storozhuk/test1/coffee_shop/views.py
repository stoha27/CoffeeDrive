from django.http import HttpResponse
from .models import UserProfile
from django.template import loader

def index(request):
    # return  HttpResponse("<h1> This is online shop</h1>")
    all_users = UserProfile.objects.all()
    template = loader.get_template('coffee_shop/index.html')
    context = {
        'all_users': all_users,
    }
    return HttpResponse(template.render(context, request))