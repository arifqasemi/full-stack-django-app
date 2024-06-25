from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    image = models.FileField(upload_to='uploads', default='default.jpg')




# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,)
#     image = models.FileField(upload_to='uploads', default='default.jpg')

# class Task(models.Model):
#     user =models.ForeignKey(User,on_delete=models.CASCADE, default=None)
#     title 					   		   = models.TextField()
#     description 				       = models.TextField()
