from django.contrib import admin

from ejercicioApp1.forms import FormProducto, FormProveedor, FormTemporada
from ejercicioApp1.models.producto import Producto
from ejercicioApp1.models.proveedor import Proveedor
from ejercicioApp1.models.temporada import Temporada

class ProductoAdmin(admin.ModelAdmin):
    form = FormProducto
    
class ProveedorAdmin(admin.ModelAdmin):
    form = FormProveedor
    
class TemporadaAdmin(admin.ModelAdmin):
    form = FormTemporada

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Temporada, TemporadaAdmin)