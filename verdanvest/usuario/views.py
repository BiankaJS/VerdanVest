from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from usuario.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from compras.models import Pedido, PedidoDetalle

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
    except Exception: 
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
    try:
        user = request.user
        pedido = Pedido.objects.filter(usuario_id=request.user.id)
        detalles_pedidos = []
        for p in pedido:
            detalles_pedido = PedidoDetalle.objects.filter(pedidoId_id=p.id)
            detalles_pedidos.append({'pedido': p, 'detalles': detalles_pedido})
        context = {
            'pedido': pedido,
            'detalles_pedidos': detalles_pedidos,
            'user': user,
        }
        return render(request, 'usuario/profile.html', context)
    except: 
        return render(request, 'usuario/profile.html')

def logout_view(request):
    logout(request)
    return redirect('auth:login')

@login_required
def addAddress_view(request):
    if request.method == 'POST':
        user = request.user
        dto = User.objects.get(pk=user.id)
        dto.domicilio = request.POST.get('address')
        dto.save()
        return redirect('auth:profile')