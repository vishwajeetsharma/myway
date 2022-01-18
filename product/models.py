from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=155)



class Promo_code(models.Model):
    code = models.CharField(max_length=6)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.IntegerField()
    limits = models.IntegerField()
    used_times = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code+" - "+str(self.discount)+"%"

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    after_discount_pirce = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    promo_codes = models.ManyToManyField(Promo_code)

    def __str__(self):
        return self.name
    