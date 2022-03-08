from django.shortcuts import render

# Create your views here.
from .models import Addresses, CountryAddressStructure
from .controller import Controller
from postalAddress import AddressesRespository

def index(request):
    """View function for home page of site"""
    # Generate counts of the addresses and countryaddressstructure
    num_addresses = Addresses.objects.all().count()
    num_countryAddressStructure = CountryAddressStructure.objects.all().count()

    # Testing whether the contoroller is working working
    get_country = Controller.Get_Country(request)

    # Tesing whether the controller is working for the Addresses
    get_addresses = Controller.Get_Address(request)

    context = {
        'num_addresses': num_addresses,
        'num_countryAddressStructure': num_countryAddressStructure,
        'get_country': get_country,
        'get_addresses': get_addresses,
    }


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def search_address(request):
    # this is coming from the index.html class
     if request.method == 'GET':
        query = request.GET.get('query')
        strQuery = str(query)
        print("testing Query")
        print("printing out the query: " + strQuery)
        listAddress = []
        if query:
            products = Controller.Get_Address(request)
            print("testing")
            print(products)
            for i in products:
                print(i)
                if strQuery in i:
                    print("printing out the query: " + strQuery)
                    print("Success!")
                    listAddress.append((i))
            return render(request,'searchAddress.html',{'listAddress': listAddress})
        else:
            print("No information to show")
            return request(request,'searchAddress.html',{})


def search_state(request):
    if request.method == 'GET':
        query = request.GET.get('query')
    listOfState = ['North Dakota']
    if query == 'North Dakota':
        state= Controller.Get_Address(request).filter(addressLine__icontains=query)
        return render(request, 'searchAddress.html', {'state': state})
    else:
        print("No information to show")
        return request(request, 'searchAddress.html', {})