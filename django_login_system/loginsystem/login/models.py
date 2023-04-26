from django.db import models

# Create your models here.

class Userdetails(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=18)

    def __str__(self):
        return self.username