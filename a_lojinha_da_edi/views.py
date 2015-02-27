from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .forms import PecaBasicForm
from catalogo.models import Peca


def admin_add_peca(request):
    if request.method == 'GET':
        form = PecaBasicForm()

    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = PecaBasicForm(request.POST)

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            nome = form.cleaned_data['nome']
            categoria = form.cleaned_data['categoria']
            peca = Peca.objects.create(nome=nome, categoria=categoria)
            return HttpResponseRedirect(reverse('admin_add_peca',
                                        kwargs={'peca_id': peca.id}))

    return render(request, 'admin_add_peca.html', {'form': form, })
