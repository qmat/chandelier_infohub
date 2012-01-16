from django.conf.urls.defaults import *
from api import UpdateResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UpdateResource())
