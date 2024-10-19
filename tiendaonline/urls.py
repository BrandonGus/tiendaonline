from django.contrib import admin
from django.urls import path
from gestionpedidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda/', views.busqueda_productos),
    path('buscar/',views.buscar),
]
