from django.shortcuts import render

# Importamos un request

from django.http import HttpResponse

# Create your views here.

def hola_mundo(request):
    # Encabezado h1
    return HttpResponse("<h1>Hola mundo desde mi aplicación web</h1>")

# Crear vista principal 

def inicio(request):
    return render(request, 'base.html')





    
