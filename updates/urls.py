from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
#import updates.views

urlpatterns = patterns('',

    url(r'^qnn/$',
        direct_to_template,
        {'template': 'updates/qnn.html'},
        name="qnn"),

)




