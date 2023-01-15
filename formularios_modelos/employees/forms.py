from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    #le indico los campos del modelo de datos asociado
    class Meta:
        model = Employee
        #fields = ['name','last_name','email']

        #o este atajo para los campos, incluye todos los campos
        fields = '__all__'

        #si quiero todos los campos excepto algunos
        #exclude = ['email']

        #si quiero agregar campos adicionales
        #extra_fields = ['salary']
