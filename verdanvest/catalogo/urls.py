from django.urls import path
from . import views

app_name='catalog'
urlpatterns = [
  path('', views.catalog, name='Catalog'),
  path('<int:categoryId>', views.catalog, name='Catalog_Id'),
  path('detail/<int:productId>', views.productDetail, name = 'ProductDetail')
]