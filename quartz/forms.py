from django import forms

class UploadSketchForm(forms.Form):
    file  = forms.FileField()
