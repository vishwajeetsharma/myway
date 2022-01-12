from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "product/home.html")

def product(request, product):
    return render(request, "product/product.html", {"Product":product})