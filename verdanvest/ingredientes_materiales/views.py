from django.shortcuts import render
from django.http import HttpResponse
from ingredientes_materiales.models import Ingrediente

def detailmaterial_view(request):
    return render(request, 'ingredientematerial/detailmaterial.html')

def detailingrediente_view(request, ingredienteId):
    ingrediente = Ingrediente.objects.get(pk=ingredienteId)
    toxicidad = int(ingrediente.toxicidad)
    print(ingrediente.toxicidad)
    context = {
        'ingrediente': ingrediente,
        'toxicidad': toxicidad
    }
    return render(request, 'detailingredientes.html', context)