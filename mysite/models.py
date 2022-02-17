from django.db import models

class AddModel(models.Model):
    street=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    state_iso= models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    country_iso=models.CharField(max_length=100)
    
    postal_code=models.IntegerField()
    
    
    class Meta:
        db_table="Adress"
