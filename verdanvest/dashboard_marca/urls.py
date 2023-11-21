from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardmarca_view, name='dashboard')
    # Otras URLs...
]