from django.db.models.fields import PositiveBigIntegerField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.user.is_authenticated:
         return redirect("/")

    if request.method == "POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        next = request.POST['next']

        user = authenticate(request, username=form_username,
                             password=form_password)

        if user is not None:
            auth_login(request, user)

            if next:
                return redirect(next)

            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")

def register(request):
    if request.user.is_authenticated:
         return redirect("/")
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

    messages.success(request, "You are successfully logged out Login Again")
    return render(request, "accounts/register.html")


@login_required(login_url="/accounts/login")
def temphome(request):
    return render(request, "accounts/home.html")


@login_required(login_url="/accounts/login")
def becomeRetailer(request):
    
    profile = Profile.objects.get(user=request.user)

    if profile.is_Retailer == True:
        return redirect(retailerWelcome)

    if request.method == "POST":
        address = request.POST['address']
        
        profile.is_Retailer = True
        profile.Address = address
        profile.save()

        return redirect(retailerWelcome)

    return render(request, "accounts/retailer.html", {"address":profile.Address})

@login_required(login_url="/accounts/login")
def retailerWelcome(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.is_Retailer:
        return render(request, "accounts/retailerDash.html")
    else:
        return redirect(becomeRetailer)

@login_required(login_url="/accounts/login")
def UserProfile(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        

        # user = User.objects.get(username = request.user.username)
        user = request.user

        profile = Profile.objects.get(user=user)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if request.FILES != 0:
            image = request.FILES['image']
            profile.DP = image

        profile.Address = address
        profile.phone = phone

        user.save()
        profile.save()

        messages.success(request, "Your data has been updated successfully")
        return render(request, "accounts/profile.html", {"profile":profile})


    return render(request, "accounts/profile.html", {"profile":profile})

def logoutPath(request):
    messages.success(request, "You are successfully logged out Login Again")
    logout(request)
    return redirect(login)