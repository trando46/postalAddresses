from django.db import models

# Create your models here.
""""
Create a table for holding the address structure of a country with the country name, 
country iso code and the address format. The address_format is a string we 
collect from the API and store as its own field. This will be used for dictating how new 
addresses must be entered for a given country when the API is called. 
"""


class CountryAddressStructure(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=100)
    address_format = models.CharField(max_length=250)  # store the structure of the country's address as a string separated by commas


"""
Create table for addresses based on country_id FK. AddressLine will hold the postal_code, state, city, and street in the 
order they are expected for the given country as a JSON field.
"""


class Addresses(models.Model):
    address_id = models.IntegerField(primary_key=True)
    country_id = models.ForeignKey(CountryAddressStructure, on_delete=models.CASCADE)  # if the FK is deleted, this enter is deleted
    addressLine = models.JSONField()


"""
This class model will allow for easier access of the JSON information in the Addresses table.
You can call the keys of the address (state, postal_code, etc.) and return the values.
All default values are empty strings
"""

class AddressLine:
    # key for postal code for any given address
    postal_code = ""

    # key for state for any given address
    state = ""

    # key for city for any given address
    city = ""

    # key for street for any given address. This field will contain the sections of the address that aren't covered by the above
    street = ""

    def __init__(self, postal_code, state, city, street):
        self.postal_code = postal_code
        self.state = state
        self.city = city
        self.street = street
