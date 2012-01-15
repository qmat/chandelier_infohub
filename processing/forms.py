from django import forms
from models import ProcessingSketch

class UploadSketchForm(forms.Form):
    file  = forms.FileField()
