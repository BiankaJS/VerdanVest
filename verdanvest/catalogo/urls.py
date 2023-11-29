from django.urls import path
from . import views

app_name='catalog'
urlpatterns = [
  path('<int:categoryId>', views.catalog, name='Catalog'),
  path('<int:productId>', views.productDetail, name = 'ProductDetail')
]