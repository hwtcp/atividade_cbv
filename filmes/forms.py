from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'diretor', 'genero', 'ano_lancamento', 'sinopse', 'assistido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'diretor': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'ano_lancamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'assistido': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
