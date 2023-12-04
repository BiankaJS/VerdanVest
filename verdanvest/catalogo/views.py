from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Producto, Categoria, Marca, ProductoIngrediente
from ingredientes_materiales.models import Material, Ingrediente
from compras.models import CarritoCompraDetalle, CarritoCompra

def productDetail(request, productId):
    try:
        product = get_object_or_404(Producto, pk=productId)
        ingredientes = ProductoIngrediente.objects.filter(producto_id=productId)
        context = {
          'product': product
        }
        return render(request, "catalogo/detailproduct.html", context)
    except Producto.DoesNotExist:
        return redirect("catalogo/catalog.html")
    except Exception as e:
        print(f"An error occurred: {e}")
        return redirect("catalogo/catalog.html", {"error_message": "Ocurred an error"})

def catalog(request, categoryId=None):
  try: 
    if categoryId is not None:
      products = Producto.objects.filter(categoria__id=categoryId)
      categoria = Categoria.objects.get(pk=categoryId)

    else:
      products = Producto.objects.all()

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

def addProductCart(request, productId):
  if(request.user):
    try: 
      cart = CarritoCompra.objects.get(usuario_id=request.user.id)
    except: 
      cart = CarritoCompra.objects.create(usuario=request.user, subtotal=0, total=0)
    if(request.method == "POST"):
      quantity = request.POST.get('quantity')
      carritoDetalle = CarritoCompraDetalle.objects.create(producto_id=productId, cantidad= quantity, carrito_compra=cart)
      carritoDetalle.save()
      return redirect('shopping:cart')
  else:
    return redirect('auth:login')