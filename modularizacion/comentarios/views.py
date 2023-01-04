from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse('Funciona correctamente Test')

def create(request):
    #Hay dos formas de crear un nuevo objeto Comment
    #comment = Comment(name='Juanjo',score=5, comment='Este es un comentario')# Forma 1
    #comment = Comment.objects.create(name='Alex')# Forma 2
    return HttpResponse('Ruta para probar la creacion de modelos')

def delete(request):
    #En base a un id borro esa informacion de la base de datos
    #comment = Comment.objects.get(id=1)# forma 1
    #comment.delete()# forma 1

    #Comment.objects.filter(id=2).delete()#forma 2
    return HttpResponse('Se ha eliminado un comentario')