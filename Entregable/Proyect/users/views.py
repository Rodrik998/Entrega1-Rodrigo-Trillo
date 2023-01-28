from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from users.models import UserProfile
from users.forms import RegisterForm, UserUpdateForm, UserProfileForm

def login_view(request): #? Funcion de inicio de sesión
    if request.method == 'GET': #? Si ingresamos por un Get nos muestra el formulario de inicio de sesion
        form = AuthenticationForm()
        context = {
            'form':form,
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
            'form':form,
        }
        return render(request, 'register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            UserProfile.objects.create(user=user)
            return redirect('login')
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
        return render(request, 'register.html', context=context)

@login_required
def UpdateUser(request):
    user = request.user
    if request.method == 'GET':
        form = UserUpdateForm(initial = {
            'username':user.username,
            'name':user.first_name,
            'last_name':user.last_name,
        })
        context = {
            'form':form
        }

    elif request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get('username')
            user.name = form.cleaned_data.get('name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
        
        context = {
            'errors':form.errors,
            'form':RegisterForm()
        }
    return render(request, 'update.html', context=context)

@login_required
def UpdateProfile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'phone':request.user.profile.phone,
            'birth_date':request.user.profile.birth_date,
            'profile_picture':request.user.profile.profile_picture
        })
        context ={
            'form':form
        }
        return render(request, 'update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'register.html', context=context)
