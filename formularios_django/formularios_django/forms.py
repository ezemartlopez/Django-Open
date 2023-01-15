from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Escribe tu nombre',max_length=100, help_text='100 caracteres maximos')
    url = forms.URLField(label='Tu sitio web', required=False, initial='http://')
    comment = forms.CharField()