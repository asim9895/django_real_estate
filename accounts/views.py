from django.shortcuts import render, redirect
from django.contrib import messages ,  auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request , user)
           messages.success(request , 'You are now logged in')
           return redirect('dashboard')
       else:
           messages.error(request, 'Invalid credentials')
           return redirect('login')

    else:
        return render(request , 'accounts/login.html')

def register(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       password = request.POST['password']
       password2 = request.POST['password2']
       email = request.POST['email']

       if password == password2:
           if User.objects.filter(username=username).exists():
               messages.error(request , 'Username taken')
               return redirect('register')
           else:
               if User.objects.filter(email=email).exists():
                   messages.error(request , 'Email Already Exists')
                   return redirect('register')
               else:
                   user = User.objects.create(username=username , first_name=first_name , last_name=last_name,
                   email=email,password=password)

                   user.set_password(password)
                   user.save()
                   messages.success(request, 'You are now registered and can log in')
                   return redirect('login')               
       else:
           messages.error(request , 'Password do not match')
           return redirect('register')
    else:
        return render(request , 'accounts/register.html')
         

def dashboard(request):
    if auth.user_logged_in:
        return render(request , 'accounts/dashboard.html')
    else:
        return redirect('index')
    
     

def logout(request):
    auth.logout(request)
    messages.success(request , 'Successfully logged out')
    return redirect('index')