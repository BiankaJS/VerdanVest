from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Producto, Categoria, Marca
from ingredientes_materiales.models import Material, Ingrediente

def productDetail(request, productId):
  try:
    product = get_object_or_404(Producto, pk=productId)
    print(product)
    return render(request, "catalogo/detailproduct.html", { 'product': product })
  except:
    return redirect("catalogo/catalog.html", {"error_message": "Ocurred an error"})
  #return render(request, "catalogo/detailproduct.html")

def catalog(request, categoryId=None):
  try: 
    if categoryId is not None:
      products = Producto.objects.filter(categoria__id=categoryId)
    else:
      products = Producto.objects.all()

    categories = Categoria.objects.all() if Categoria is not None else []
    brandies = Marca.objects.all() if Marca is not None else []
    materials = Material.objects.all() if Material is not None else []
    ingredients = Ingrediente.objects.all() if Ingrediente is not None else []

    context = {
      'products': products,
      'categories': categories,
      'brandies': brandies,
      'materials': materials,
      'ingredients': ingredients
    }

    return render(request, 'catalog.html', context)
  except: 
    products = Producto.objects.all()
    categories = Categoria.objects.all() if Categoria is not None else []
    brandies = Marca.objects.all() if Marca is not None else []
    materials = Material.objects.all() if Material is not None else []
    ingredients = Ingrediente.objects.all() if Ingrediente is not None else []

    context = {
      'products': products,
      'categories': categories,
      'brandies': brandies,
      'materials': materials,
      'ingredients': ingredients
    }
    return render(request, 'catalogo/catalog.html', context)