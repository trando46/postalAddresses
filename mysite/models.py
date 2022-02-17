from django.db import models

# This is the model class for the address 
class AddModel(models.Model):
    
    #### This need to be removed later 
    #street=models.CharField(max_length=100)
    #city= models.CharField(max_length=100)
    #state=models.CharField(max_length=100)
    #street=models.CharField(max_length=100)
    #state_iso= models.CharField(max_length=100)
    #country=models.CharField(max_length=100)
    #country_iso=models.CharField(max_length=100)
    #postal_code=models.IntegerField()
    
    def getStreet():
        return models.CharField(max_length=100) 

    def getCity():
        return models.CharField(max_length=100)
    
    def getState():
        return models.CharField(max_length=100)
    
    def getStateISO():
        return models.CharField(max_length=100)
    
    def getCountry():
        return models.CharField(max_length=100)
    
    def getCountryISO():
        return models.CharField(max_length=100)
    
    def getPostalCode():
        return models.CharField(max_length=100)

