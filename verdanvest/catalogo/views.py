from django.shortcuts import render, get_object_or_404, redirect
from catalogo.models import Producto

def productDetail(request):
  # try:
  #   product = get_object_or_404(Producto, pk=1)
  #   return render(request, "catalogo/detailproduct.html", {})
  # except:
  #   return redirect("catalogo/catalog.html", {"error_message": "Ocurred an error"})
  return render(request, "catalogo/detailproduct.html", {""})

def catalog(request, categoryId=None):
  try: 
    if categoryId is not None:
      products = Producto.objects.filter(categoria__id=categoryId)
    else:
      products = Producto.objects.all()
    context = {
      'products': products,
      'categoryId': categoryId
    }
    return render(request, 'catalog.html', context)
  except: 
    request.session['alerta'] = 'Categoría no válida.'
    alerta = request.session.pop('alerta', None)
    context = {'alerta': alerta}
    return render(request, 'catalogo/catalog.html', context)