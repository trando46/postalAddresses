from django.db import models
import entry_type_enum

# Create your models here.
""""
Create a table for holding the address structure of a country with the country name, 
country iso code and the address format. The address_format is a JSON string we 
collect from the API and store as it's own field, converted to an Array field based 
on the FormatFields Model to extract the correct structure and address references

EX: JP -> Postal, Prefecture, Municipal, Address Line 2, Address Line 1.
EX: MX -> Address Line, Settlement, Postal, Municipality, Federal Entity
"""
class AddressStructure(models.Model):
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=100)
    address_format = models.JSONField()

"""
This class model will create the JSON string to hold the format
of the country address
"""
class FormatFields:
    # What type of entry in the form this will be. Default is default(0)
    field_type = entry_type_enum.FormEntry.DEFAULT

    # key value for referencing the address field by the correct name. Default is empty
    key = ""

    # Name of the address field to display to user. Default is empty
    display_name = ""

    # bool for whether or not the field is required. Default is true
    optional = True

    def __init__(self, type, key, display, optional):
        self.field_type = type
        self.key = key
        self.display_name = display
        self.optional = optional

"""
Create a table for storing all country's states/prefectures/provinces/etc.

Using State as our variable to reference the values for each country's version,
but display name will be dependent on the key from address_format_model.py as we require 
this data to create a new country
"""
class CountryTerritories(models.Model):
    country = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    #meta is for database table connection
    class Meta:
        db_table="sample1"