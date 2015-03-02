from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import PecaForm

from catalogo.models import Peca, QuantidadeDePecasPorTamanho


def admin_estoque_nova_peca(request):
    QuantidadeFormSet = inlineformset_factory(Peca, QuantidadeDePecasPorTamanho)
    if request.method == 'POST':
        form_principal = PecaForm(request.POST, request.FILES)
        quantidade_formset = QuantidadeFormSet(request.POST, instance='Peca')

        if form_principal.is_valid() and quantidade_formset().is_valid():
            form_principal.save(commit=True)
            quantidade_formset.save(commit=True)
            return HttpResponseRedirect('/superadmin/')
    else:
        form_principal = PecaForm(prefix='peça')
        quantidade_formset = QuantidadeFormSet()

    return render_to_response('admin_nova_peca.html', {
        'form_principal': form_principal,
        'quantidade_formset': quantidade_formset,
    })