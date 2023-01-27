from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(req, letter = None):
    '''Esta parte para obtener las letras de los contactos, puede hacerse de manera mas eficiente
    es decir puedo crear una estructura global (un array), pero este debe modificarse cuando se 
    hace una edicion, una creacion y un borrado de un contacto. Por ahora se carga cada vez que se
    ingresa a la pagina index, ya sea con una letra de busqueda o no'''
    contact_filter = Contact.objects.all()
    letters_filter = [contact.name[0].upper() for contact in contact_filter]
    letters_filter.sort()
    #========================================================================
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith = letter)
    else:
        contacts = Contact.objects.filter(name__contains = req.GET.get('search',''))
    context ={
        'contacts':contacts,
        'letters':letters_filter
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