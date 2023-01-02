from django.http import HttpResponse
from django.shortcuts import render

def simple(request):
    # Basico
    # 1ro Informacion de peticion, 2do plantilla y 3ro contexto
    return render(request, 'simple.html', {})

def dinamico(request, name):
    # Pasando contexto al llamado de la url
    categorias = ['code','design','marketing']
    context = {
        'name':name,
        'categorias':categorias
    }
    return render(request, 'dinamico.html',context)