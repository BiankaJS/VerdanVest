from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Producto, Categoria, Marca, ProductoIngrediente, ProductoMaterial
from ingredientes_materiales.models import Material, Ingrediente
from compras.models import CarritoCompraDetalle, CarritoCompra
from django.contrib.auth.decorators import login_required

def productDetail(request, productId):
    try:
        product = get_object_or_404(Producto, pk=productId)
        ingredients = ProductoIngrediente.objects.filter(producto_id=productId)
        recomend = Producto.objects.exclude(pk=productId)[:4]
        context = {
          'product': product,
          'ingredients': ingredients,
          'recomend': recomend
        }
        return render(request, "catalogo/detailproduct.html", context)
    except Producto.DoesNotExist:
        return redirect("catalogo/catalog.html")
    except Exception as e:
        print(f"An error occurred: {e}")
        return redirect("catalogo/catalog.html", {"error_message": "Ocurred an error"})

def catalog(request):
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

def catalog_category(request, categoryId):
  try: 
    dto = Producto.objects.all()
    print(dto)
    products = dto.filter(categoria_id=categoryId)
    print(products)
    categoria = Categoria.objects.get(pk=categoryId)

    categories = Categoria.objects.all() if Categoria is not None else []
    brandies = Marca.objects.all() if Marca is not None else []
    materials = Material.objects.all() if Material is not None else []
    ingredients = Ingrediente.objects.all() if Ingrediente is not None else []

    context = {
      'categoria': categoria.nombre,
      'products': products,
      'categories': categories,
      'brandies': brandies,
      'materials': materials,
      'ingredients': ingredients
    }

    return render(request, 'catalogo/catalog.html', context)
  except: 
    categories = Categoria.objects.all() if Categoria is not None else []
    brandies = Marca.objects.all() if Marca is not None else []
    materials = Material.objects.all() if Material is not None else []
    ingredients = Ingrediente.objects.all() if Ingrediente is not None else []

    context = {
      'products': [],
      'categories': categories,
      'brandies': brandies,
      'materials': materials,
      'ingredients': ingredients
    }
    return render(request, 'catalogo/catalog.html', context)

def catalog_brand(request, brandId):
  try: 
    dto = Producto.objects.all()
    print(dto)
    products = dto.filter(marca_id=brandId)
    print(products)

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
  except: 
    categories = Categoria.objects.all() if Categoria is not None else []
    brandies = Marca.objects.all() if Marca is not None else []
    materials = Material.objects.all() if Material is not None else []
    ingredients = Ingrediente.objects.all() if Ingrediente is not None else []

    context = {
      'products': [],
      'categories': categories,
      'brandies': brandies,
      'materials': materials,
      'ingredients': ingredients
    }
    return render(request, 'catalogo/catalog.html', context)

def addProductCart(request, productId):
  if(request.user.id):
    try: 
      user = request.user
      cart = CarritoCompra.objects.get(usuario_id=user.id)
    except: 
      cart = CarritoCompra.objects.create(usuario=request.user, subtotal=0, total=0)
    if(request.method == "POST"):
      quantity = request.POST.get('quantity')
      carritoDetalle = CarritoCompraDetalle.objects.create(producto_id=productId, cantidad= quantity, carrito_compra=cart)
      carritoDetalle.save()
      return redirect('shopping:cart')
  else:
    return redirect('auth:login')