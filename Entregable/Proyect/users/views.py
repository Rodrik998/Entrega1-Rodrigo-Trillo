from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from users.models import UserProfile
from users.forms import RegisterForm #UserUpdateForm, UserProfileForm

def login_view(request): #? Funcion de inicio de sesión
    if request.method == 'GET': #? Si ingresamos por un Get nos muestra el formulario de inicio de sesion
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'login.html', context=context)
    
    elif request.method == 'POST': #? Si ingresamos por POST valida  que el inicio de sesion sea con los datos registrados.
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {
                    'message':f'Bienvenido {username}!!!'
                }
                return render(request, 'index.html', context=context)

def register(request): #? Funcion de creación de usuario
    if request.method == 'GET':
        form = RegisterForm()
        context ={
            'form':form
        }
        return render(request, 'register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            UserProfile.objects.create(user = user)
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'register.html', context=context)