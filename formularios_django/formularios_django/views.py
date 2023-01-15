from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm,ContactForm
def form(request):
    comment_form = CommentForm({'name':'Juanjo', 'url':'http://openbootcamp.com', 'comment':'Un comentario'})
    return render(request, 'form.html',{'comment_form':comment_form})

def goal(request):
    if(request.method != 'POST'):
        return HttpResponse('Metodo no permitido')
    return HttpResponse(request.POST['name'])
    #return render(request, '')

def widget(request):
    contact_form = ContactForm()
    return render(request,'widget.html',{'contact_form':contact_form})
