from django.conf.urls.defaults import *
import doorbell.views

urlpatterns = patterns('',

    url(r'^activate/$',
        doorbell.views.activate,
        name="activate_doorbell"),

)




