from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .forms import PecaForm


def admin_add_peca(request):
    if request.method == 'GET':
        form = PecaForm()

    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = PecaForm(request.POST)

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            return HttpResponseRedirect(reverse('admin_add_peca'))

    return render(request, 'admin_add_peca.html', {'form': form, })
