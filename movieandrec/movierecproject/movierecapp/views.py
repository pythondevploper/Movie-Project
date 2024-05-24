from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages,auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
from . models import Movieclub




# Create your views here.
def index(request):
    data = Movieclub.objects.all()
    return render(request,'index.html',{'result':data})

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)   
       if user is not None:
          auth.login(request, user)
          return redirect('/')
       else:
           messages.info(request,'invalid credentials')
           return redirect('/')
    return render(request,'login.html')
           
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return render(request,'registration.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return render (request,'registration.html')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email)
            user.save()
            return redirect('movierecapp:login')        
    return render(request,'registration.html')

def details(request):
    data = Movieclub.objects.all()
    context={
     'movielist':data   
    }
    return render(request, 'details.html',context)