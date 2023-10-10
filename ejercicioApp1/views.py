from importlib import reload
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from ejercicioApp1.forms import FormProducto

from ejercicioApp1.models.producto import Producto

# Create your views here.
def menu_principal(request):
    return render(request,'templatesApp1/menu_administrador.html')

def lista_productos(request):
    productos = Producto.objects.all()
    data = {'productos':productos}
    return render(request,'templatesApp1/lista_productos.html', data)

def agregar_producto(request):
    if request.method == 'POST':
        print(request.POST)
        form = FormProducto(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('lista_productos')
    else:
        form = FormProducto()
        form.fields.get('proveedor').empty_label = "Seleccione un proveedor"
        return render(request, 'templatesApp1/agregar_producto.html', {'form': form})

def actualizar_producto(request, id_producto):
    this_product = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=this_product)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = FormProducto(instance=this_product)
        print(form.fields.get('temporadas').choices)
    return render(request, 'templatesApp1/actualizar_producto.html', {'form': form})

def eliminar_producto(request, id_producto):
    this_product = get_object_or_404(Producto, id_producto=id_producto)
    if request.method == 'POST':
        this_product.delete()
        return redirect('lista_productos')
    return render(request, 'templatesApp1/eliminar_producto.html', {'producto': this_product})