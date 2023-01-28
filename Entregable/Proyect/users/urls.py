from django.contrib.auth.views import LogoutView
from django.urls import path

from Proyect.views import index
from users.views import login_view, register, UpdateUser, UpdateProfile

urlpatterns = [
    path('', index, name='index'),

    path('login/', login_view, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html')),
    path('register/', register, name = 'register'),
    path('update/', UpdateUser, name = 'update'),
    path('update-profile/', UpdateProfile, name = 'update profile'),
]
