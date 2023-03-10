from django.urls import path

from Products.views import create_product, list_products, add_provider, list_providers, create_category, list_categories

urlpatterns = [
    path('crear/', create_product, name = "crear producto"),
    path('listar/', list_products, name = "listar productos"),
    path('añadir-proveedor/', add_provider, name = "añadir proveedor"),
    path('ver-proveedores/', list_providers, name = 'list_providers.html'), #?Es la unica que tiene limite para las cuentas que no sean admin
    path('crear-categorias/', create_category, name = "crear categorias"),
    path('ver-categorias/', list_categories, name = "listar categorias"),
]
