from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def message(req):
    messages.success(req, 'Hola soy un mensaje exitoso')
    return render(req, 'messages.html',{})