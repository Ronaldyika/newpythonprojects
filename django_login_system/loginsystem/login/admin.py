from django.contrib import admin
from .models import Userdetails

# Register your models here.

class admin(admin.ModelAdmin):
    list_display = ('username','email','password')
    
    admin.site.register(Userdetails)