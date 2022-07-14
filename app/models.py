from django.db import models



# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut del tutor')
    nommascota = models.CharField(max_length=20, verbose_name='Nombre de la mascota')
    nomtutor = models.CharField(max_length=20, verbose_name='Nombre del tutor')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    telefono= models.IntegerField(verbose_name='Telefono')
    descripcion = models.CharField(max_length=500, verbose_name='Descripcion del pedido')
    


    def str(self):
        return self.rut

class DatosCliente(models.Model):
    rutreg = models.CharField(primary_key=True, max_length=10, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    telefono= models.IntegerField(verbose_name='Telefono')
    


    def str(self):
        return self.rutreg

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def _str_(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True, verbose_name='Id del producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def _str_(self):
        return self.idProducto    


    

    

