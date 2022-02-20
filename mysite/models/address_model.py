from django.db import models

"""
This is the model class for the address. Inherits from the Django model
class
"""

class AddressModel(models.Model):
    #TODO: Need a method for getting a full address, not just parts of an address
    #TODO: We should have a constructor no?

    def getStreet(self):
        return models.CharField(max_length=100) 

    def getCity(self):
        return models.CharField(max_length=100)
    
    def getState(self):
        return models.CharField(max_length=100)
    
    def getStateISO(self):
        return models.CharField(max_length=100)
    
    def getCountry(self):
        return models.CharField(max_length=100)
    
    def getCountryISO(self):
        return models.CharField(max_length=100)
    
    def getPostalCode(self):
        return models.CharField(max_length=100)

