from django.shortcuts import render, redirect
from .models import Producto
from django.contrib import messages

def home(request):
    return render(request, "AppCoder/padre.html") 

def consultar(request):
    #variable = tabla.objetos.todos
    productos  = Producto.objects.all()
    return render(request, "AppCoder/productos.html",{
        'productos ': productos ,
    })

def guardar(request):
    #name en producto.html
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    #nueva variable = Modelo(izquierda, nombre en models.variable a la que hacemos referencia)
    p = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
    #guardar datos 
    p.save()
    messages.success(request, 'Producto guardado correctamente')
    #redireccionar a otra pagina
    return redirect('productos:consultar')

def eliminar(request, id):
    #ir por el producto
    #variable = tabla.objetos.filtro
    producto  = Producto.objects.get(pk=id)
    producto .delete()
    messages.success(request, 'Producto eliminado correctamente')
    #redireccionar a otra pagina
    return redirect('productos:consultar')

def detalle(request, id):
    productos = Producto.objects.get(pk=id)
    return render(request, "AppCoder/productoEditar.html", {
        'productos'  : productos 
        })