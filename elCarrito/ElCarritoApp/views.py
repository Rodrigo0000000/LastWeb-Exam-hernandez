from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from ElCarritoApp.carrito import Carrito
from ElCarritoApp.models import Producto
from .models import Producto, Usuario

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos': productos})

def index(request):
    return render(request, 'index.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def registrar_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        correo_electronico = request.POST.get('correo_electronico')
        ciudad = request.POST.get('ciudad')
        contrasena = request.POST.get('contrasena')

        usuario = Usuario.objects.create(
            nombre_usuario=nombre_usuario,
            correo_electronico=correo_electronico,
            ciudad=ciudad,
            contrasena=contrasena
        )
        usuario.save()

        return render(request, 'registro_exitoso.html', {'usuario': usuario})

    return render(request, 'registro_usuario.html')
