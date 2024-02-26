from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import ProfForm
from users.models import Profile


# Create your views here.

def register(request):
    
    if request.method == 'POST':
     form = RegisterForm(request.POST)
     if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(
           request,
           'Welcome {}, Your account has been sussessfully created. Now you may login below'.format(username)
        )
        return redirect('login') 
    else:
        form = RegisterForm()  

    
    context = {
      'form':form
     }

    return render(request, 'users/register.html', context)


def login_view(request):
   
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      if (username == '') or (username is None):
         username = User.objects.get(email=email)
      user = authenticate(request, username=username, password=password)
   
      if user is None:
         messages.success(
           request,
           'Invaid user, try again'.format(user)
        ) 
         return redirect('login')

      elif user.is_superuser:
         login(request,user)
         messages.success(
           request,
           'Welcome {}, Your account superuser has been logged in  sussessfully'.format(user)
        )
         return redirect('Eshop:index')
      elif user is not None:
      
         login(request, user)

         messages.success(
           request,
           'Welcome {}, Your account has been logged in  sussessfully'.format(user)
        )
         
         return redirect('Eshop:index')
   
   return render(request, 'users/login.html')

def logout_view(request):
   
   if request.method == 'POST':
      user = request.user.username
      logout(request)
      messages.success(
        request,
        'Welcome {}, Your account hass been logged out successfully.'.format(user)
      )
      return redirect('Eshop:index')
   return render(request, 'users/logout.html')


def ProfilePage(request):

   prof = Profile.objects.get(user= request.user.id)
   

   if not request.user.is_authenticated:

      return redirect('login')
   
   context = {
      'prof': prof
   }

   return render(request, 'users/profile.html', context)


def ProfileForm(request, prof_id):

   prof = Profile.objects.get(id=prof_id)
   form = ProfForm(request.POST or None, request.FILES or None, instance=prof)
   
   if request.method == 'POST':
      form.save()
      return redirect('Eshop:index')

   context = {
      'form':form

   }

   return render(request, 'users/profform.html', context)





    
   
