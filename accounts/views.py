from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def login(request):
    return HttpResponse("Hello World login")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        number = request.POST['number']
        password = request.POST['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        profile=Profile.objects.create(user=user, phone=number)
        profile.save()
        

        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        
        messages.success(request, "You Have successfully registered in our website")
        return redirect("/accounts/home")
    return render(request, "accounts/register.html")

def temphome(request):
    return render(request, "accounts/home.html")