from django.shortcuts import render
from django.http  import HttpResponse

def form(request):
    return render(request, 'form.html',{})

def goal(request):
    if(request.method != 'GET'):
        return HttpResponse(' El metodo post no esta soportado')
    print(dir(request.GET))
    name = request.GET['name']
    message = request.GET['message']
    return render(request, 'success.html',{'name':name, 'message': message})
    
    

