from django import forms
from processing.models import ProcessingSketch
#from utils.web import rurl
from django.contrib.sites.models import Site
from quartz.models import QuartzSketch
from models import WebViewPreset


class URLOrProcessingWidget(forms.TextInput):

    def __init__(self, attrs=None):
        # options for dropdown, also be sure to set the Site in the admin
        # N.B. can't use rurl because it causes circular imports
        processing_sketches = [('http://%s/processing/sketch/%s' % \
                                (Site.objects.get_current().domain, sk.name), sk.name) \
                               for sk in ProcessingSketch.objects.all()]
        processing_sketches = [('', '')] + processing_sketches
        self.processing_widget = forms.Select(attrs=None, choices=processing_sketches)
        super(URLOrProcessingWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        result =  super(URLOrProcessingWidget, self).render(name, value, attrs)
        result += self.processing_widget.render('%s_proc' % name, None, None)
        return result

class WebViewPresetForm(forms.Form):
    name = forms.CharField()
    views = forms.IntegerField()
    url_1 = forms.CharField(widget=URLOrProcessingWidget)
    url_2 = forms.CharField(widget=URLOrProcessingWidget, required=False)
    url_3 = forms.CharField(widget=URLOrProcessingWidget, required=False)
    url_4 = forms.CharField(widget=URLOrProcessingWidget, required=False)
    url_5 = forms.CharField(widget=URLOrProcessingWidget, required=False)
    url_6 = forms.CharField(widget=URLOrProcessingWidget, required=False)
    url_7 = forms.CharField(widget=URLOrProcessingWidget, required=False)
    url_8 = forms.CharField(widget=URLOrProcessingWidget, required=False)


class ChangeScreenForm(forms.Form):
    # load the choices dynamically
    def __init__(self, *args, **kwargs):
        super(ChangeScreenForm, self).__init__(*args, **kwargs)
        self.fields['quartz_sketch'] = forms.ChoiceField(required=False, choices=[('', '')] + [(o.file.path, o.name) for o in QuartzSketch.objects.all()] )
        self.fields['web_preset'] = forms.ChoiceField(required=False, choices=[('', '')] + [(o.name, o.name) for o in WebViewPreset.objects.all()])
