from django.urls import path
from . import views

app_name='catalog'
urlpatterns = [
  path('<int:categoryId>', views.catalog, name='Catalog'),
  path('detail/', views.productDetail, name = 'ProductDetail')
]