from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Proyect.views import index
from users.views import login_view, register

urlpatterns = [
    path('', index, name='index'),

    path('login/', login_view, name = 'Login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html')),
    path('register/', register, name = 'Register'),
]
