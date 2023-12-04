from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:Home')
            else:
                error_message = "Invalid email or password. Please try again."
                return render(request, 'usuario/login.html', {'error_message': error_message})
        return render(request, 'usuario/login.html')
    except Exception as e:
        print(f"Error en el login: {e}")   
        return render(request, 'usuario/login.html')

def register_view(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.date_joined = timezone.now()
            user.role = 1
            user.save()
            return redirect('auth:login')
        else:
            return render(request, 'usuario/register.html')
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return render(request, 'usuario/register.html')

@login_required
def profile_view(request):
    return render(request, 'usuario/profile.html')


def logout_view(request):
    logout(request)
    return redirect('home:Home')
