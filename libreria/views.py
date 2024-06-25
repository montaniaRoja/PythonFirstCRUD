from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


# Create your views here.


def libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'libros/index.html', {'libros': libros})


def crear(request):
    return render(request, 'libros/crear.html')


def editar(request):
    return render(request, 'libros/editar.html')
