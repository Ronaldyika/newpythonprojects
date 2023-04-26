from django.shortcuts import render,redirect
from .models import Userdetails
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
#creating the index page

def index(request):
    users = Userdetails.objects.all()
    

    context = {
        'index': users
    }



    return render(request,'index.html',context)


#view functiion for the signup

def signup(request):

    userfields = Userdetails()

    if request.method == 'POST':
        username = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']

        details = userfields(username = username, email = email, password = password)

        details.save()

        return redirect('signin')
    else:


        return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,username=username,email=email,password=password)

        if user is not None:
    
            login(request,user)

            return redirect('index')
        else:
           # messages.error('bad request')

            return render(request,'signin.html')

