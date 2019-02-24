from django import forms

class FileUploadCnmbForm(forms.Form):
    file = forms.FileField()
