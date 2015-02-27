from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'a_lojinha_da_edi.views.home', name='home'),

    url(r'^superadmin/', include(admin.site.urls)),
    url(r'^admin', 'a_lojinha_da_edi.views.admin', name='admin'),
)
