from django.urls import path
from . import views

app_name='detail'
urlpatterns = [
    path('material/', views.detailmaterial_view, name='detailmaterial'),
    path('ingrediente/<int:ingredienteId>', views.detailingrediente_view, name='detailingrediente')
]
