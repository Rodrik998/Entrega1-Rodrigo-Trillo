from django.contrib import admin
from django.urls import path

from Products.views import create_product, list_products, add_provider, list_providers, create_category, list_categories

urlpatterns = [
    path('crear/', create_product, name = "Crear producto"),
    path('listar/', list_products, name = "Listar productos"),
    path('añadir-proveedor/', add_provider, name = "Añadir proveedor"),
    path('ver-proveedores/', list_providers, name = "Ver proveedores"),
    path('crear-categorias/', create_category, name = "Crear categorias"),
    path('ver-categorias/', list_categories, name = "Listar categorias"),
]
