from django.urls import path
from . import views

app_name='detail'
urlpatterns = [
    path('detailmaterial/', views.detailmaterial_view, name='detailmaterial'),
    path('detail', views.detailingrediente_view, name='detailingrediente')
]
