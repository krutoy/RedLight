# import sys
# sys.path.append('..')
# import redlight.settings
from redlight import settings
from django.conf.urls import *
from raasite.views import *

urlpatterns = patterns('',
			url(r'^$', index),
			url(r'^members/', members),
			url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATICFILES_DIRS}),
)
