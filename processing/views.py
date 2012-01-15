from models import ProcessingSketch
from forms import UploadSketchForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse, \
    HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from utils.web import rtr, rurl



# Imaginary function to handle an uploaded file.
def __handle_uploaded_file(f):
    sketch, _ = ProcessingSketch.objects.get_or_create(name=f.name)
    sketch.text = ''.join(f.readlines())
    sketch.name = f.name
    sketch.save()
    return f.name

def upload_sketch(request):
    if request.method == 'POST':
        form = UploadSketchForm(request.POST, request.FILES)
        if form.is_valid():
            sketch_name = __handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(rurl('view_sketch_code', sketch_name))
    else:
        form = UploadSketchForm()
    return rtr('processing/upload.html')


def view_sketch_code(request, sketch):
    sketch = get_object_or_404(ProcessingSketch, name=sketch)
    return rtr('processing/sketch_code.html')

def raw_sketch(request, sketch):
    sketch = get_object_or_404(ProcessingSketch, name=sketch)
    return HttpResponse(sketch.text)

def raw_sketch_random(request):
    sketch = ProcessingSketch.objects.order_by('?')[0]
    return HttpResponse(sketch.text)

def view_sketch(request, sketch):
    sketch = get_object_or_404(ProcessingSketch, name=sketch)
    return rtr('processing/sketch.html')

def view_sketch_random(request):
    sketch = ProcessingSketch.objects.order_by('?')[0]
    return rtr('processing/sketch.html')
