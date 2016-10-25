from django.http import HttpResponse
from .models import UserProfile
from django.shortcuts import render

def index(request):
    # return  HttpResponse("<h1> This is online shop</h1>")
    all_users = UserProfile.objects.all()
    context = {'all_users': all_users}
    return render(request, 'registr/index.html', context)

def detail(request, UserProfile_id):
    return HttpResponse("<h2>Details for UserProfile id: " + str(UserProfile_id) + "</h2>")