from django import forms
from catalogo.models import CategoriaDaPeca


class PecaBasicForm(forms.Form):
    CATEGORIA_CHOICES = CategoriaDaPeca.objects.values_list('id', 'categoria')

    nome = forms.CharField(max_length=30)
    categoria = forms.MultipleChoiceField(choices=CATEGORIA_CHOICES)
