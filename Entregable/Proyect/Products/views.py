from django.shortcuts import render
from django.http import HttpResponse

from Products.models import products, category, providers
from Products.forms import ProductForms, CategoryForms, ProviderForms

def create_product(request):
    if request.method == 'GET': #? Si el programa esta entrando por un metodo 'get' mostramos el formulario de create_product.html
        context = {
            'form': ProductForms()
        }
        return render (request, 'create_products.html', context = context)

    elif request.method == 'POST': #?Si entramos por metdo 'post' se valida que los datos ingresados sean correctos antes de mostrar el formulario
        form = ProductForms(request.POST)
        if form.is_valid():
            products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                stock = form.cleaned_data['stock'],
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

def list_products(request): 
    if 'search' in request.GET:
        Search = request.GET["Search"]
        Products = products.object.filter(name__icontains = Search)
    else:
        Products = products.objects.all()
        context = {
                'products': Products,
            }
    return render(request, "list_products.html", context = context)

def list_categories(request):
    all_categories = category.objects.all()
    context = {
        'categories':all_categories,
    }
    return render(request, "list_categories.html", context=context)

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

def list_providers(request):
    all_providers = providers.objects.all()
    context = {
        'providers': all_providers,
    }
    return render(request, "list_providers.html", context=context)
