from django.http import HttpResponse

def holaMundo(request):
    return HttpResponse('Hola Mundo')