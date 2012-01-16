# urls.py
from django.conf.urls.defaults import *
import processing.views

urlpatterns = patterns('',

    url(r'^upload/$',
        processing.views.upload_sketch,
        name="upload_sketch"),

    url(r'^code/(?P<sketch>[^//]+)/$',
        processing.views.view_sketch_code,
        name="view_sketch_code"),

    url(r'^raw/random/$',
        processing.views.raw_sketch_random,
        name="random_raw_sketch"),

    url(r'^raw/(?P<sketch>[^//]+)$',
        processing.views.raw_sketch,
        name="raw_sketch"),

    url(r'^sketch/random/$',
        processing.views.view_sketch_random,
        name="view_sketch"),

    url(r'^sketch/(?P<sketch>[^//]+)$',
        processing.views.view_sketch,
        name="view_sketch"),
)




