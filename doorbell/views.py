from django.http import HttpResponse
from utils.quatz import web_mode

def activate(request):
    #web_mode(1, ['http://127.0.0.1:8000/static/doorbell_stream.html'])
    web_mode(8, ['http://10.0.2.1/~MAT/ipcamimages/index.html'])
    return HttpResponse('')
