from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        # get the post parameters
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
       #Checks for signup
        myuser = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        return redirect('/shop')
    else:
       return render(request, 'accounts/signup.html')

def handlelogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        myuser = authenticate(username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "You Are Successfully Logged in,Please Continue to Checkout")
            return redirect('/shop/checkout')
        elif messages.error(request, "Invalid Credentials"):
            return redirect('/')
        else:
            return HttpResponse("404 error found")
    return render(request, 'accounts/login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!!")
    return redirect('/')
    return HttpResponse("handlelogout")
