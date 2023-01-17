from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def index(req):
    contacts = Contact.objects.filter(name__contains = req.GET.get('search',''))
    context ={
        'contacts':contacts
    }
    return render(req, 'contact/index.html',context=context)