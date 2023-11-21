from django.urls import path
from . import views

urlpatterns = [
  path('', views.catalog, name='Catalog'),
  path('<int:categoryId>', views.productDetail, name = 'ProductDetail')
]