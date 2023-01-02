from django.http import HttpResponse
from django.shortcuts import render

def simple(request):
    # Basico
    # 1ro Informacion de peticion, 2do plantilla y 3ro contexto
    return render(request, 'simple.html', {})