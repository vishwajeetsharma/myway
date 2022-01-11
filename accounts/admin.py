from django.contrib import admin
from . import models
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_Retailer', 'phone']

admin.site.register(models.Profile, ProfileAdmin)