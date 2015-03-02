from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import nova_peca

urlpatterns = patterns('',
    # url(r'^$', 'a_lojinha_da_edi.views.home', name='home'),
    url(r'^superadmin/', include(admin.site.urls)),
    # url(r'^admin/', 'a_lojinha_da_edi.views.admin_estoque', name='estoque'),
    # url(r'^admin/estoque/', 'a_lojinha_da_edi.views.admin_estoque', name='estoque'),
    url(r'^admin/estoque', nova_peca.as_view(), name='nova_peca'),
    )
