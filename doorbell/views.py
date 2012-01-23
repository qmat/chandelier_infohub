from django.http import HttpResponse
from utils.quatz import doorbell_mode

def activate(request):
    doorbell_mode()
    return HttpResponse('')
