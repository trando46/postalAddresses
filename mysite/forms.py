from django import forms
from mysite.address_model import AddressModel

#
class Addforms(forms.ModelForm):
    class Meta:
        model=AddressModel
        fields="__all__"
