from django.shortcuts import render
from django.http import HttpResponse

def dashboardmarca_view(request):
    return render(request, 'dashboardmarca/dashboard.html')
