from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .forms import PecaForm, QuantidadeFormSet
from catalogo.models import Peca


class nova_peca(CreateView):
    model = Peca
    template_name = "admin_nova_peca.html"
    form_class = PecaForm
    success_url = "estoque/nova/peca/"

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        quantidade_form = QuantidadeFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  quantidade_form=quantidade_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        quantidade_form = QuantidadeFormSet(self.request.POST)

        if form.is_valid() and quantidade_form.is_valid():
            return self.form_valid(form, quantidade_form)

        else:
            return self.form_invalid(form, quantidade_form)

    def form_valid(self, form, quantidade_form):
        self.object = form.save()
        quantidade_form.isntance = self.object
        quantidade_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, quantidade_form):
        return self.render_to_response(self.get_context_data(form=form,
                                       quantidade_form=quantidade_form))
