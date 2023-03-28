from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'core/inicio.html')


def tienda(request):
    return render(request, 'core/tienda.html')


def generos(request):
    return render(request, 'core/generos.html')


def about(request):
    return render(request, 'core/about.html')


def login_view(request):
    return render(request, 'core/login.html')


def register_view(request):
    return render(request, 'core/register.html')