from django.http import HttpResponse
from utils.quatz import web_mode

def activate(request):
    web_mode(8, ['http://admin:@127.0.0.1:8000/static/doorbell_stream.html'])
    return HttpResponse('')
