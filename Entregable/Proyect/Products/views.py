from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Proyect.decorators import user_is_admin

from Products.models import products, category, providers
from Products.forms import ProductForms, CategoryForms, ProviderForms


@user_is_admin
def create_product(request):
    if request.method == 'GET': #? Si el programa esta entrando por un metodo 'get' mostramos el formulario de create_product.html
        context = {
            'form': ProductForms()
        }
        return render (request, 'create_products.html', context = context)
    elif request.method == 'POST': #?Si entramos por metodo 'post' se valida que los datos ingresados sean correctos antes de mostrar el formulario
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock'],
                image = form.cleaned_data['image'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'create_products.html', context=context)
        else: 
            context = {
                'form_errors': form.errors,
                'form': ProductForms()
            }
            return render(request, 'create_products.html', context=context)

@user_is_admin
def create_category(request):
    if request.method == 'GET':
        context = {
            'form': CategoryForms()
        }
        return render(request, "create_category.html", context = context)

    elif request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            category.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
            )
            context = {
                'message': 'Categoria creada exitosamente'
            }
            return render(request, "create_category.html", context = context)
        else:
            context = {
                'form_errors': form.errors,
                'form': CategoryForms()
            }
            return render(request, "create_category.html", context = context)

@login_required
def list_products(request): 
    if 'search' in request.GET:
        search = request.GET['search']
        Products_list = products.objects.filter(name__icontains = search)
    else:
        Products_list = products.objects.all()
    context = {
            'products': Products_list,
        }
    return render(request, "list_products.html", context=context)

@login_required
def list_categories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_categories = category.objects.filter(name__icontains = search)
    else:
        all_categories = category.objects.all()
    context = {
        'categories':all_categories,
    }
    return render(request, "list_categories.html", context=context)

@user_is_admin
def add_provider(request):
    if request.method == 'GET':
        context = {
            'form': ProviderForms()
        }
        return render (request, "add_provider.html", context=context)
    elif request.method == 'POST':
        form = ProviderForms(request.POST)
        if form.is_valid():
            providers.objects.create(
                name = form.cleaned_data['name'],
                provides = form.cleaned_data['provides'],
            )
            context = {
                'message': 'Proveedor añadido con éxito'
            }
            return render (request, "add_provider.html", context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProviderForms()
            }
            return render(request, "create_category.html", context = context)


@user_is_admin
def list_providers(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_providers = providers.objects.filter(name__icontains = search)
    else:
        all_providers = providers.objects.all()
    context = {
        'providers': all_providers,
    }
    return render(request, "list_providers.html", context=context)

