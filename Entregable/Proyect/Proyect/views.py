from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

def aboutUs(request):
    return render(request, 'contact.html', context={})
