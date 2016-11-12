from django.http import HttpResponse
from .models import UserProfile
from django.shortcuts import render

def index(request):
    all_users = UserProfile.objects.all()
    return render(request, 'registr/index.html', {'all_users': all_users})

def detail(request, UserProfile_id):
    return HttpResponse("<h2>Details for UserProfile id: " + str(UserProfile_id) + "</h2>")