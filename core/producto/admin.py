from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","descripcion","precio","cantidad","disponible","fecha_creacion")
    list_filter=("disponible","precio")
    search_fields=("nombre","descripcion")

admin.site.register(Producto,ProductoAdmin)