from django.db import models
from django.contrib.postgres.fields import ArrayField

""""
Create a table for holding the address format of a country
with the country name, country iso code and the address format
which is passed through the api as a JSON array and converted an
array field based on the FormatField Model
"""
class CountryAddressFormat(models.Model):
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=100)
    #address_format = ArrayField(ArrayField(models.)

"""
This class model will create the field to hold the format
of the country model based on an array
"""
class FormatFields(models.Model):
    