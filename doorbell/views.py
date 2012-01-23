from django.http import HttpResponse
from utils.quatz import start_doorbell_mode

def activate(request):
    start_doorbell_mode()
    return HttpResponse('')
