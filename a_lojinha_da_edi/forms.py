from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from catalogo.models import Peca


class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(field_labels)s devem ser únicos.",
            }
        }
