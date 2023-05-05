from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
database = []
def home(request):
    if request.method == "POST":
        email = request.POST['email']
        database = email
        print(database)
    return render(request,'home.html')

def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been successfully login')
            redirect('home')
        else:
            messages.success(request,"Try again later")
    return render(request,'singIn.html')