from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'usuario/login.html')

def register_view(request):
    return render(request, 'usuario/register.html')
