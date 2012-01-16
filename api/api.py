from tastypie.resources import ModelResource
from updates.models import Update

class UpdateResource(ModelResource):
    class Meta:
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        queryset = Update.objects.order_by('-timestamp')
        resource_name = 'update'
