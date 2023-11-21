from django.urls import path
from . import views

urlpatterns = [
    path('detailproduct/', views.detailproduct_view, name='detailproduct')
    # Otras URLs...
]