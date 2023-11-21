from django.urls import path
from . import views

urlpatterns = [
    path('detailmaterial/', views.detailmaterial_view, name='detailmaterial')
    # Otras URLs...
]
