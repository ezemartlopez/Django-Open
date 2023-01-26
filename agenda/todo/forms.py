from django.forms import ModelForm, DateInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        #fields = '__all__'
        exclude = ('date', )
        #Dando formato a estimated_end, para css
        widgets = {
            'estimated_end': DateInput(attrs={'type':'date'}),
        }