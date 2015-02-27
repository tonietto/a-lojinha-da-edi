from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'a_lojinha_da_edi.views.home', name='home'),

    url(r'^superadmin/', include(admin.site.urls)),
    url(r'^admin/add_peca', 'a_lojinha_da_edi.views.admin_add_peca', name='add_peca'),
)
