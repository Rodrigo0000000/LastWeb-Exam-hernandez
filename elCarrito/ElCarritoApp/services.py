from .models import Producto
from django.shortcuts import render

def obtener_productos():
    return Producto.objects.all()