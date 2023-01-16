from django.contrib import admin
from .models import Product

# Register your models here.

#Clase de administracion del producto en modo administrador
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','short_description', 'stock',)#elementos de la clase producto que queremos visualizar
    search_fields = ('name','short_description',)#campos que se utilizaran en la busqueda
    list_filter = ('name','stock','discount_until',)#campos que se utilizaran como filtros
    date_hierarchy = 'discount_until' #seguimiento de fechas crea agrupaciones para facilitar la busqueda

#Al producto le paso esta clase, para visualizar la info requerida
admin.site.register(Product,ProductAdmin)