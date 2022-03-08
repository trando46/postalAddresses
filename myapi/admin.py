from django.contrib import admin
from .models import CountryAddressStructure
from .models import Addresses
from .models import States

# Register your models here.
"""
Adding our DB tables to our admin UI in Django
"""

admin.site.register(CountryAddressStructure)
admin.site.register(Addresses)
admin.site.register(States)
