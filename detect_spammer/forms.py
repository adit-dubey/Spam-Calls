from django import forms
from .models import DetectSpammer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = DetectSpammer
        fields = ['name', 'phone_number', 'email',]

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)
