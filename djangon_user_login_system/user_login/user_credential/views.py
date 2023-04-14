from django.shortcuts import render
from .models import register
from .models import login

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'nav/body.html')
def register(request):
    if request.method == 'post':
        firstname = request.post['firstname']
        lastname = request.post['lastname']
        username = request.post['username']
        password = request.post['password']
        passwordconfirmation = request.post['password']
        if(password == passwordconfirmation):

            newuser = register(username,password)
            newuser.save()
            print('successfull signup')
            return redirect('../main/landing.html')
            

        else:
            return redirect('../main/landing.html')

    return render(request,'main/landing.html')
def home(request):
    return render(request,'main/home.html')

    ##info about the login page
def login(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']

        if(login.username == index.username):
            if(login.password == index.password):
                return redirect(home)
            else:
                return redirect(login)
                
        else:
            return redirect(register)

    return render(request,'main/login.html')
