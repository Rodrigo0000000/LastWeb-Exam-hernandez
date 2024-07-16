# ElCarritoApp/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    ciudad = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario
    