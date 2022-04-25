from django import forms
from .models import *

class AddTextFileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control form-control-sm'}))
    unique_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    unique_number = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

    class Meta:
        model = AddTextFile
        fields = ['file', 'unique_title', 'unique_number']