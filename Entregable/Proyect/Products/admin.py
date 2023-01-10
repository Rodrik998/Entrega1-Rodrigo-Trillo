from django.contrib import admin

from Products.models import products, category, providers

admin.site.register(products)
admin.site.register(category)
admin.site.register(providers)
