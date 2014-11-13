from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'redlight.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('raasite.urls')),
    #url(r'^members/', include('raasite.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
