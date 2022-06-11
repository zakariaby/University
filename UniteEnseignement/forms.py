from django import forms

from .models import *

class CycleForm(forms.ModelForm):
    themes = forms.ModelMultipleChoiceField(queryset=Niveau.objects, widget=forms.CheckboxSelectMultiple(), required=False)
