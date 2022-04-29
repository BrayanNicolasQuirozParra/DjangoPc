from django.shortcuts import render,redirect
from pc.models import Producto
# Create your views here.

def list(request):
    return render(request, "inicio/inicio.html")

def list_producto(request):
    productos = Producto.objects.all()
    return render(request, "inicio/inicio.html", {"productos": productos})

def crear(request):
    if request.method == "GET":
        return render(request,"inicio/crear.html")
    imagen = request.FILES["imagen_producto"]
    nombre = request.POST["nombre_producto"]
    marca = request.POST["marca_producto"]
    precio = request.POST["precio_producto"]

    producto = Producto.objects.get(id=1)

    guardar_pc = Producto(imagen= imagen, nombre=nombre, marca=marca, precio=precio)
    guardar_pc.save()

    return redirect('inicio:list_inicio')


