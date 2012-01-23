from django.conf.urls.defaults import *
import administration.views

urlpatterns = patterns('',

    url(r'^presets/$',
        administration.views.list_presets,
        name="list_presets"),

    url(r'^presets/new/$',
        administration.views.new_preset,
        name="new_web_preset"),

    url(r'^presets/(?P<name>[^//]+)/edit/$',
        administration.views.edit_preset,
        name="edit_web_preset"),

    url(r'^presets/(?P<name>[^//]+)/$',
        administration.views.view_preset,
        name="view_web_preset"),

    url(r'^screen/$',
        administration.views.change_screen,
        name="change_screen"),

)




