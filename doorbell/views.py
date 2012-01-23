from django.http import HttpResponse
from utils.quatz import web_mode

def new_preset(request):
    web_mode(8, ['http://127.0.0.1:8000/static/doorbell_stream.html'])
    return HttpResponse('')
