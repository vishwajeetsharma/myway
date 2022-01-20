from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from product.models import Product
from django.contrib import messages
# Create your views here.
def home(request):
    profile = Profile.objects.get(user=request.user)
    products = Product.objects.filter(availablity=True)

    context = {
        "profile_photo":profile.DP,
        "products": products
    }
    return render(request, "product/home.html", context)

def product(request, product):
    return render(request, "product/product.html", {"Product":product})


@login_required(login_url="/accounts/login")
def PublishProduct(request):
    profile = Profile.objects.get(user=request.user)
    if profile.is_Retailer:
        if request.method == "POST":
            user = request.user
            name = request.POST['name']
            description = request.POST['description']
            # take category 
            discount = request.POST['discount']
            after_discount_pirce = request.POST['after_discount_pirce']

            product = Product.objects.create(
                user = user,
                name = name,
                description = description,
                discount = discount,
                after_discount_pirce = after_discount_pirce
            )

            product.save()

            messages.success(request, "Product added succesfully")
            return render(request, "product/retailer/publish_product.html")

        return render(request, "product/retailer/publish_product.html")
    return redirect("/accounts/become-a-retailer/")