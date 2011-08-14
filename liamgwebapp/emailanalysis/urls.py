from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('emailanalysis.views',
    (r'^$', 'index'),
    (r'^(?P<datatype>[\w]+)/json/$', 'getjson'),
    (r'^sendmail/$', 'sendmail'),
    (r'^sendmail/send/$', 'sendmail'),
    (r'^test/$', direct_to_template, {'template': 'emailanalysis/testautocomplete.html'}),
                       
    # Examples:
    # url(r'^$', 'liamgwebapp.views.home', name='home'),
    # url(r'^liamgwebapp/', include('liamgwebapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
