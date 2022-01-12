from django.contrib import admin
from .models import Category, Product, Promo_code
# Register your models here.
admin.site.register(Category)
admin.site.register(Promo_code)
admin.site.register(Product)