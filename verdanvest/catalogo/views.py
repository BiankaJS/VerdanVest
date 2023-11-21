from django.shortcuts import render
from django.http import HttpResponse

def detailproduct_view(request):
    return render(request, 'catalogo/detailproduct.html')

