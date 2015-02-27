# from django.catalogo.models import Peca
# from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext

from .forms import PecaForm


def admin(request):

    form = PecaForm()

    return render_to_response("admin.html", locals(), context_instance=RequestContext(request))
