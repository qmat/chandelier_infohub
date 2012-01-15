from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import processing.views

urlpatterns = patterns('',

    url(r'^processing/upload/$',
        processing.views.upload_sketch,
        name="upload_sketch"),

    url(r'^processing/code/(?P<sketch>[^//]+)/$',
        processing.views.view_sketch_code,
        name="view_sketch_code"),

    url(r'^processing/raw/random/$',
        processing.views.raw_sketch_random,
        name="random_raw_sketch"),

    url(r'^processing/raw/(?P<sketch>[^//]+)$',
        processing.views.raw_sketch,
        name="raw_sketch"),

    url(r'^processing/sketch/random/$',
        processing.views.view_sketch_random,
        name="view_sketch"),

    url(r'^processing/sketch/(?P<sketch>[^//]+)$',
        processing.views.view_sketch,
        name="view_sketch"),





    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
