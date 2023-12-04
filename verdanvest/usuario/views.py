from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import User

def login_view(request):
    return render(request, 'usuario/login.html')

def register_view(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('usernameInput')
            first_name = request.POST.get('firstNameInput')
            last_name = request.POST.get('lastNameInput')
            email = request.POST.get('emailInput')
            password = request.POST.get('passwordInput')
            user = User.objects.create(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.date_joined = timezone.now()
            print(user)
            user.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/register.html')
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return render(request, 'usuario/register.html')

def profile_view(request):
    return render(request, 'usuario/profile.html')

