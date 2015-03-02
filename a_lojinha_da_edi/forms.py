from django.forms import ModelForm

from catalogo.models import Peca, QuantidadeDePecasPorTamanho


class PecaForm(ModelForm):
    class Meta:
        model = Peca


class QuantidadeForm(ModelForm):
    class Meta:
        model = QuantidadeDePecasPorTamanho
