from django.db import models
from django.contrib.auth.models import AbstractUser

# Customer user model
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    is_vendor = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null= True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# User address model
class Address(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)