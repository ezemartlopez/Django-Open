from django.shortcuts import render
from django.http import HttpResponse

from .models import Publication, Article

# Create your views here.
def create(request):
    '''
    #Para relacionar objetos muchos a muchos deber estar guardados en la base de datos
    #ya que la recion se hace en la base de datos con el id de los objetos y si no estan guardados, no se pueden relacionar
    art1 = Article(headline='Articulo Primero')
    art1.save()

    art2 = Article(headline='Articulo Segundo')
    art2.save()

    art3 = Article(headline='Articulo Tercero')
    art3.save()

    pub1 = Publication(title='Publicacion Primera')
    pub1.save()
    pub2 = Publication(title='Publicacion Segunda')
    pub2.save()
    pub3 = Publication(title='Publicacion Tercera')
    pub3.save()
    pub4 = Publication(title='Publicacion Cuarta')
    pub4.save()
    pub5 = Publication(title='Publicacion Quinta')
    pub5.save()
    pub6 = Publication(title='Publicacion Sexta')
    pub6.save()
    pub7 = Publication(title='Publicacion Septima')
    pub7.save()

    #Hacemos las relaciones 
    art1.publication.add(pub1)
    art1.publication.add(pub2)
    art1.publication.add(pub3)
    art2.publication.add(pub4)
    art2.publication.add(pub5)
    art3.publication.add(pub6)
    art3.publication.add(pub7)
'''
    #result = art1.publication.all()

    #accedo al objeto de la base de datos por su id
    pub1 = Publication.objects.get(id=1)
    #Ahora accedo a que articulo pertenece segun la base de datos muchos a muchos
    result = pub1.article_set.all()
    #Obtengo el articulo de id 3
    art = Article.objects.get(id=3)
    #ahora borramos la publicacion 6
    pub = Publication.objects.get(id=7)
    #lo elimno la publicacion de la relacion de la base de datos muchos a muchos
    art.publication.remove(pub)
    #Lo que hace es eliminar la relacion los objetos todavia existen
    result = art.publication.all()
    return HttpResponse(pub)