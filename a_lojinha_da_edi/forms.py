from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from catalogo.models import Peca, QuantidadeDePecasPorTamanho


class PecaForm(ModelForm):
    class Meta:
        model = Peca

QuantidadeFormSet = inlineformset_factory(Peca, QuantidadeDePecasPorTamanho)
