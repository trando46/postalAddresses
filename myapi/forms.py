from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import CountryAddressStructure

# Create a country address structure form
from myapi.models import CountryAddressStructure
from myapi.models import Addresses
class CountryAddressStructureforms(forms.ModelForm):
    class Meta:
        model=CountryAddressStructure
        fields="__all__"

class Addressesforms(forms.ModelForm):
    class Meta:
        model=Addresses
        fields="__all__"
