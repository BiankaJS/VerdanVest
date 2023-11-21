from django.shortcuts import render
from django.http import HttpResponse

def detailmaterial_view(request):
    return render(request, 'ingredientematerial/detailmaterial.html')

