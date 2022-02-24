from django import forms
from postal_address.models.address_model import AddressModel
# https://www.javatpoint.com/django-forms#:~:text=Django%20provides%20a%20Form%20class,how%20it%20works%20and%20appears.&text=Each%20field%20of%20the%20form,validation%20while%20submitting%20the%20form.
#
class Addforms(forms.ModelForm):
    class Meta:
        model=AddressModel
        fields="__all__"
