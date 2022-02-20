from django.db import models

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
