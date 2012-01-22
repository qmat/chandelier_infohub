from django.conf.urls.defaults import patterns, include, url
from api.urls import v1_api
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import DEBUG
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',

    (r'^processing/',
     include('processing.urls')),

    (r'^quartz/',
     include('quartz.urls')),

    (r'^updates/',
     include('updates.urls')),

    (r'^administration/',
     include('administration.urls')),

    (r'^api/',
     include(v1_api.urls)),

    url(r'^streetview/$',
        direct_to_template,
        {'template': 'streetview/streetview.html'},
        name="qnn"),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if DEBUG:
    urlpatterns += staticfiles_urlpatterns()

