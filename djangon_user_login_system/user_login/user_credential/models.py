from django.db import models

# Create your models here.

class register(models.Model):
    firsname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=13)
    password = models.CharField(max_length=15)
    comfirmpassword = models.CharField(max_length=15)

class login(models.Model):
    username = models.CharField(max_length=13)
    password = models.CharField(max_length=15)