from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

# Create your views here.
def queries(req):
    #Obtener todos los elementos
    authors = Author.objects.all()
    #obtener datos filtrados por condicion, en este caso el email seleccionado
    email = 'cody58@example.net'
    filtered = Author.objects.filter(email=email)

    #Obtenemos un objeto (filtrado)
    author = Author.objects.get(id=2)

    #Obtener los 12 primeros elementos
    limit = Author.objects.all()[:12]

    #obtener 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    #Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    #Obtener todos los elementos cuto id sea menor o igual a 15
    filtered2 = Author.objects.filter(id__lte = 15)

    #Obtener todos los autores que contienen en su nombre la palabra yes
    filtered3 = Author.objects.filter(name__contains='yes')

    context = {
        'authors':authors, 
        'filtered':filtered,
        'email_filtered':email,
        'author':author,
        'limit':limit,
        'offsets':offsets,
        'orders':orders,
        'filtered2':filtered2,
        'filtered3':filtered3
    }
    return render(req, 'post/queries.html',context)