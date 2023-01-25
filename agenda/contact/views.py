from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

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
    contact = Contact.objects.get(id=id)
    if(req.method == 'GET'):
        
        form = ContactForm(instance=contact)
        context = {'form':form, 'id':id}
        return render(req,'contact/edit.html',context)
    if(req.method == 'POST'):
        form = ContactForm(req.POST, instance=contact)
        #vemos si el formulario recibido es valido
        if(form.is_valid()):
            form.save()
        context = {'form':form, 'id':id}
        #agrego un mensage, y los tags son en este caso las clases que tienen los mensajes(ver como se implementan)
        messages.success(req,message='Contacto actualizado.', extra_tags='alert-success')
        return render(req,'contact/edit.html',context)

def create(req):
    if(req.method =='GET'):
        form = ContactForm()
        context = {'form': form}
        return render(req,'contact/create.html',context)
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')

def delete(req,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')