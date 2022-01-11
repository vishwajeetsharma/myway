from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_Retailer = models.BooleanField(default=False)
    phone = models.IntegerField()
    DP = models.ImageField(upload_to="DP/", null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username
    