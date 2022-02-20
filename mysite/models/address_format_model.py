from django.db import models
from django.contrib.postgres.fields import ArrayField
from mysite.enums import entry_type_enum

""""
Create a table for holding the address format of a country with the country name, 
country iso code and the address format. The address_format is a JSON string we 
collect from the API and store as it's own field, converted to an Array field based 
on the FormatFields Model to extract the correct structure and address references

EX: JP -> Postal, Prefecture, Municipal, Address Line 2, Address Line 1.
EX: MX -> Address Line, Settlement, Postal, Municipality, Federal Entity
"""
class CountryAddressFormat(models.Model):
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=100)
    address_format = ArrayField(ArrayField(models.CharField(max_length=1024, blank=False)))

"""
This class model will create the field to hold the format
of the country model based on an array
"""
class FormatFields(models.Model):
    # What type of entry in the form this will be
    field_type = models.CharField(
        choices=entry_type_enum.FormEntry.choices,
        default=entry_type_enum.FormEntry.DEFAULT,
    )

    # key value for referencing the address field by the correct name
    key = models.CharField(max_length=100)

    # Name of the address field to display to user
    display_name = models.CharField(max_length=100)

    # bool for whether or not the field is required
    optional = models.BooleanField
