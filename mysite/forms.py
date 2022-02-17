from django import forms
from mysite.models import AddModel

class Addforms(forms.ModelForm):
    class Meta:
        model=AddModel
        fields="__all__"
