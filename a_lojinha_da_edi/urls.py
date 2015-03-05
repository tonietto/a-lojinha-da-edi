from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
                       '',
                       (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
                       url(r'^$', include(admin.site.urls)),  # admin site
                       url(r'^admin/', include(admin.site.urls)),  # admin site
                       url(r'^admin/catalogo', include(admin.site.urls), name='catalogo'),  # admin site
                       )
'''
url(r'^$', 'a_lojinha_da_edi.views.home', name='home'),
'''
