from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Proyect.settings import MEDIA_ROOT, MEDIA_URL
from Proyect.views import index, contact, aboutUs

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contacto/', contact, name='contacto'),
    path('sobre-mi/', aboutUs, name='sobre mi'),

    path('productos/', include('Products.urls')),
    path('usuario/', include('users.urls')),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
