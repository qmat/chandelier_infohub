from models import QuartzSketch
from forms import UploadSketchForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from utils.web import rtr, rurl


def upload_sketch(request):
    if request.method == 'POST':
        form = UploadSketchForm(request.POST, request.FILES)
        if form.is_valid():
            sketch_name = request.FILES['file'].name
            sketch, _ = QuartzSketch.objects.get_or_create(name=sketch_name)
            sketch.name = sketch_name
            sketch.file = request.FILES['file']
            sketch.save()
            return HttpResponseRedirect(rurl('view_quartz_sketch', sketch.name))
    else:
        form = UploadSketchForm()
    return rtr('quartz/upload.html')


def view_quartz_sketch(request, sketch):
    sketch = get_object_or_404(QuartzSketch, name=sketch)
    return rtr('quartz/sketch.html')

def list_sketches(request):
    sketches = QuartzSketch.objects.all()
    return rtr('quartz/sketches.html')
