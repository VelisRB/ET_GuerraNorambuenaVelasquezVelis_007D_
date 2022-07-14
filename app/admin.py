from django.contrib import admin
from .models import Cliente, DatosCliente, Categoria, Producto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(DatosCliente)
admin.site.register(Categoria)
admin.site.register(Producto)