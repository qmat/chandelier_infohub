# urls.py
from django.conf.urls.defaults import *
import quartz.views

urlpatterns = patterns('',

    url(r'^upload/$',
        quartz.views.upload_sketch,
        name="upload_quartz_sketch"),

    url(r'^sketch/(?P<sketch>[^//]+)$',
        quartz.views.view_quartz_sketch,
        name="view_quartz_sketch"),
)




