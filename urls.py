from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from siam.views import index, getEnv
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
    url(r'^siam/getEnv/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', getEnv),
    url(r'^siam/authUser/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', authUser),
    url(r'^siam/contactUs/$', contactUs),
    url(r'^siam/executeAction/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<idAction>\w+)/(?P<idDev>\w+)/(?P<param>\w+)/(?P<idEnv>\w+)$', executeAction),
    url(r'^siam/getDevByEnv/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<idEnv>\w+)$', getDevByEnv),
    url(r'^siam/getMonitorByDev/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<date\w+>)/(?P<idDev>\w+)$', getMonitorByDev),
    url(r'^siam/getReportByDev/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<date\w+>)/(?P<idDev>\w+)$', getReportByDev),
    url(r'^siam/getReport/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<date\w+>)/(?P<idEnv>\w+)/(?P<idDev>\w+)/(?P<idUser>\w+)$', getReport),
    url(r'^siam/getProfile/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', getProfile),
    url(r'^siam/panicActive/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', panicActive),
    url(r'^siam/panicInfo/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', panicInfo),
    url(r'^siam/setDevice/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<device>\w+)$', setDevice),
    url(r'^siam/setProfileActive/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<device>\w+)$', setProfileActive),
    url(r'^siam/getStatusByDev/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<idEnv>\w+)/(?P<idDev>\w+)$', getStatusByDev),
    url(r'^siam/getMessageReport/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', getMessageReport),
    url(r'^siam/getPassKey/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)$', getPassKey),
    url(r'^siam/getTpDev/(?P<user>\w+)/(?P<password>\w+)/(?P<version>\w+)/(?P<idTpDev>\w+)$', getTpDev),
    url(r'^siam/newPassword/(?P<user>\w+)$', newPassword),
    url(r'^siam/sendPassword/(?P<email>\w+)$', sendPassword),

#    executeReverseCommand(xs:string user, xs:string pass, xs:string version, xs:int idDev, xs:int idEnv, )
#    getReservReport(xs:string user, xs:string pass, xs:string version, )
#    setStPassKey(xs:string user, xs:string pass, xs:string version, xs:int idPassKey, xs:int action, )
)
