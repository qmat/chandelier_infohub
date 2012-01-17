from django import forms
from processing.models import ProcessingSketch
from utils.web import rurl
from django.contrib.sites.models import Site



class URLOrProcessingWidget(forms.TextInput):

    def __init__(self, attrs=None):
        # options for dropdown, also be sure to set the Site in the admin
        # N.B. can't use rurl because it causes circular impors
        processing_sketches = [('http://%s/processing/raw/%s' % \
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


