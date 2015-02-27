from django.forms import ModelForm
from catalogo.models import Peca


class PecaForm(ModelForm):
    class Meta:
        model = Peca
