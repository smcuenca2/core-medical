from django import forms

class FileUploadUmlsForm(forms.Form):
    file = forms.FileField()
