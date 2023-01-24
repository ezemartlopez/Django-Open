from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
# Create your views here.

def index(req):
    contacts = Contact.objects.filter(name__contains = req.GET.get('search',''))
    context ={
        'contacts':contacts
    }
    return render(req, 'contact/index.html',context=context)

def view(req, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact':contact
    }
    return render(req,'contact/detail.html',context)

def edit(req,id):
    if(req.method == 'GET'):
        contact = Contact.objects.get(id=id)
        form = ContactForm(instance=contact)
        context = {'form':form}
        return render(req,'contact/create.html',context)
