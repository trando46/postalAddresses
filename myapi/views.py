from django.shortcuts import render

# Create your views here.
from .models import Addresses, CountryAddressStructure
from .apiController import Controller
from postalAddress import AddressesRespository

"""
This function is for viewing the content in our database 
"""
def index(request):
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
    return render(request, 'base_generic.html', context=context)

"""
This function does the querying for the user inputs for the addresses and give the match back 
"""
def search_address(request):
    # this is coming from the index.html class
     if request.method == 'GET':
        query = request.GET.get('query')
        country = request.GET.get('country')
        strCountry = str(country).lower()
        strQuery = str(query).lower()
        print("testing Query")
        print("printing out the query: " + strQuery)
        listAddress = []
        products = Controller.Get_Address(request)
        if query == '':
            for i in products:
                print(i)
                x = i.lower()
                if strQuery in x:
                    print("testing the strquery condition")
                    if strCountry in x:
                        print("printing out the query: " + strQuery)
                        print("Success!")
                        listAddress.append((i))
            print(country)
            print(listAddress)
            return render(request, 'searchAddress.html', {'listAddress': listAddress})

        if country == "DEFAULT":
            for i in products:
                print(i)
                x = i.lower()

                if strQuery in x:
                    print("testing the strquery condition")

                    print("printing out the query: " + strQuery)
                    print("Success!")
                    listAddress.append((i))
            print(country)
            print(listAddress)
            return render(request,'searchAddress.html',{'listAddress': listAddress})

        if query:
            print("testing")
            print(products)
            for i in products:
                print(i)
                x = i.lower()

                if strQuery in x:
                    print("testing the strquery condition")
                    if strCountry in x:
                        print("printing out the query: " + strQuery)
                        print("Success!")
                        listAddress.append((i))
            print(country)
            print(listAddress)
            return render(request,'searchAddress.html',{'listAddress': listAddress})
        else:
            print("No information to show")
            return request(request,'searchAddress.html',{})

