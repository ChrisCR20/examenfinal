from django.db import models
from django.contrib import admin
from django.utils import timezone

class Producto(models.Model):
    codigo = models.IntegerField(default=0)
    nombre  = models.CharField(max_length=30)
    marca = models.PositiveSmallIntegerField(default = 0)
    precio = models.DecimalField(default=1.0,max_digits=5,decimal_places=2)
    existencia = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre    = models.CharField(max_length=60)
    dpi      = models.CharField(max_length=60)
    productos   = models.ManyToManyField(Producto, through='Compra')

    def __str__(self):
        return self.nombre

class Compra (models.Model):
     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
     cantidad = models.IntegerField(default=0)
     fecha = models.DateTimeField(blank=True, null=True)
     codigo_p = models.IntegerField(default=0)
     

     def __str__(self):
         return self.cantidad

class CompraInLine(admin.TabularInline):
    model = Compra
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (CompraInLine,)


class UsuarioAdmin (admin.ModelAdmin):
    inlines = (CompraInLine,)


def marca_str(self):
		if self.marca== 0 :

			return "Apple"

		if self.marca == 1:
			return "Sony"

		if self.marca == 2:
			return "Nike"

		return "Sin definir"

def comprar(self):
            self.fecha = timezone.now()
            self.save()
