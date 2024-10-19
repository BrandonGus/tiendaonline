from django.contrib import admin

from gestionpedidos.models import client, articulos, pedidos

class clientesadmin(admin.ModelAdmin):
    list_display=('nombre','direccion','telefono')
    search_fields=('nombre','direccion','telefono')
    list_filter=('nombre','direccion','telefono')

class articulosadmin(admin.ModelAdmin):
    list_display=("nombre",'seccion','precio')
    list_filter=("nombre",'seccion','precio')
    search_fields=("nombre",'seccion','precio')

class pedidosadmin(admin.ModelAdmin):
    list_display=("numero",'fecha','entregado')
    search_fields=("numero",'fecha','entregado')
    list_filter=("numero",'fecha','entregado')
    date_hierarchy="fecha"

admin.site.register(client, clientesadmin)
admin.site.register(articulos, articulosadmin)
admin.site.register(pedidos, pedidosadmin)

