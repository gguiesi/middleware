from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from siam.views import index
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'middleware.views.home', name='home'),
    # url(r'^middleware/', include('middleware.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^siam/$', index),
)
