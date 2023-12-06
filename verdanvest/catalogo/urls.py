from django.urls import path
from . import views

app_name='catalog'
urlpatterns = [
  path('', views.catalog, name='Catalog'),
  path('category/<int:categoryId>', views.catalog_category, name='Catalog_category'),
  path('brand/<int:brandId>', views.catalog_brand, name='Catalog_brand'),
  # path('ingredient/<int:ingredientId>', views.catalog_ingredient, name='Catalog_ingredient'),
  # path('material/<int:materialId>', views.catalog_material, name='Catalog_material'),
  path('detail/<int:productId>', views.productDetail, name ='ProductDetail'),
  path('add/<int:productId>', views.addProductCart, name='addProductCart')
]