from django.shortcuts import render

# Create your views here.
from .models import Addresses, CountryAddressStructure

def index(request):
    """View function for home page of site"""
    # Generate counts of the addresses and countryaddressstructure
    num_addresses = Addresses.objects.all().count()
    num_countryAddressStructure = CountryAddressStructure.objects.all().count()

    context = {
        'num_addresses': num_addresses,
        'num_countryAddressStructure': num_countryAddressStructure,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

