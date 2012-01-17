from models import WebViewPreset
from forms import WebViewPresetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from utils.web import rtr, rurl
import json

def __save_preset(form):
    if form.is_valid():
        urls = []
        for i in range(8):
            if form.cleaned_data['url_%s' % (i+1)]:
                urls.append(form.cleaned_data['url_%s' % (i+1)])

        preset, _ = WebViewPreset.objects.get_or_create(name=form.cleaned_data['name'])
        preset.views=form.cleaned_data['views']
        preset.urls = json.dumps(urls)
        preset.save()
        return HttpResponseRedirect(rurl('view_web_preset', preset.name))
    else:
        return False


def new_preset(request):
    if request.method == 'POST':
        form = WebViewPresetForm(request.POST)
        result = __save_preset(form)
        if result:
            return result
    else:
        form = WebViewPresetForm()
    return rtr('administration/edit_preset.html')


def edit_preset(request, name):
    preset = WebViewPreset.objects.get(name=name)
    if request.method == 'POST':
        form = WebViewPresetForm(request.POST)
        result = __save_preset(form)
        if result:
            return result
    else:
        urls = json.loads(preset.urls)
        urls_d = {}
        for i in range(len(urls)):
            urls_d['url_%s' % (i+1)] = urls[i]
        form = WebViewPresetForm(initial=dict({'name': preset.name,
                                               'views': preset.views}.items() +
                                              urls_d.items()))
    return rtr('administration/edit_preset.html')


def view_preset(request, name):
    preset = WebViewPreset.objects.get(name=name)
    urls = json.loads(preset.urls)
    return rtr('administration/view_preset.html')

