from django.http import HttpResponse

def holaMundo(request):
    return HttpResponse('Hola Mundo')
def adulto(request, edad):
    if(edad >= 18):
        return HttpResponse('Eres mayor de edad.')
    else:
        return HttpResponse('No eres mayor de edad.')

def home(request):
    return HttpResponse('Bienvenido a la pagina principal.')