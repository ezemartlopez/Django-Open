from django.shortcuts import render

# Create your views here.
def optional(req,name = 'Nombre por defecto'):
    return render(req, 'optional.html', {'name':name})