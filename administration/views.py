from models import WebViewPreset
from forms import WebViewPresetForm, ChangeScreenForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from utils.web import rtr, rurl
from utils.quatz import web_mode, quartz_mode, open_quatz, quit_quatz
import json

def __save_preset(form):
    if form.is_valid():
        urls = []
        for i in range(8):
            if form.cleaned_data['url_%s' % (i+1)]:
                urls.append(form.cleaned_data['url_%s' % (i+1)])

        try:
            preset = WebViewPreset.objects.get(name=form.cleaned_data['name'])
        except WebViewPreset.DoesNotExist:
            preset = WebViewPreset()
        preset.name=form.cleaned_data['name']
        preset.views = form.cleaned_data['views']
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

def change_screen(request):
    if request.POST:
        form = ChangeScreenForm(request.POST)
        if form.is_valid():
            # turning the screen off
            if form.cleaned_data['on_or_off'] == 'off':
                quit_quatz()
            # turning it on or changing it
            else:
                if form.cleaned_data['on_or_off'] == 'on':
                    open_quatz()
                if form.cleaned_data['quartz_sketch']:
                    quartz_mode(form.cleaned_data['quartz_sketch'])
                elif form.cleaned_data['web_preset']:
                    preset = WebViewPreset.objects.get(name=form.cleaned_data['web_preset'])
                    urls = json.loads(preset.urls)
                    web_mode(preset.views, urls)
    else:
        form = ChangeScreenForm()
    return rtr('administration/change_screen.html')


def list_presets(request):
    presets = WebViewPreset.objects.all()
    return rtr('administration/presets.html')
