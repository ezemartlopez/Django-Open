from django.shortcuts import render
from django.http  import HttpResponse

def getform(request):
    return render(request, 'form.html',{})

def getgoal(request):
    if(request.method != 'GET'):
        return HttpResponse(' El metodo post no esta soportado')
    print(dir(request.GET))
    name = request.GET['name']
    message = request.GET['message']
    return render(request, 'success.html',{'name':name, 'message': message})
    
def postform(request):
    return render(request,'postform.html',{})

def postgoal(request):
    if(request.method != 'POST'):
        return HttpResponse('El metodo GET no esta permitido.')
    info = request.POST['info']
    return render(request,'postsuccess.html',{'info': info})
    

