from django.shortcuts import render, redirect
from soporte.models import Contacto

def home(request):
  try: 
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      message = request.POST.get('message')
      contacto = Contacto(nombre=name, telefono=phone, email=email, mensaje=message)
      contacto.save()
      message = 'Message send!'
      return render(request, 'contact.html', {'message': message})
    else:
      return render(request, 'contact.html')  
  except: 
    return render(request, 'contact.html')