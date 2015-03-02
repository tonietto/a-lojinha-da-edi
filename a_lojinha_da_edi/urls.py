from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^$', 'a_lojinha_da_edi.views.home', name='home'),
    url(r'^superadmin/', include(admin.site.urls)),
    # url(r'^admin/', 'a_lojinha_da_edi.views.admin_estoque', name='estoque'),
    # url(r'^admin/estoque/', 'a_lojinha_da_edi.views.admin_estoque', name='estoque'),
    url(r'^admin/estoque/nova/peca', 'a_lojinha_da_edi.views.admin_estoque_nova_peca', name='nova_peca'),
    )
