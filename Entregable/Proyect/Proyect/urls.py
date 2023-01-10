from django.contrib import admin
from django.urls import path, include

from Proyect.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('productos/', include('Products.urls')),
]
