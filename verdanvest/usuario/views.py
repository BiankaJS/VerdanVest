from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import User

def login_view(request):
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
            user.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/register.html')
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return render(request, 'usuario/register.html')

def profile_view(request):
    return render(request, 'usuario/profile.html')


