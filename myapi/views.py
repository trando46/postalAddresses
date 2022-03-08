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
        state = request.GET.get('state')
        strCountry = str(country).lower()
        strQuery = str(query).lower()
        strState = str(state).lower()
        print("testing Query")
        print("printing out the query: " + strQuery)
        listAddress = []
        products = Controller.Get_Address(request)

        get_country = Controller.Get_Country(request)
        get_state = Controller.Get_States(request)

        context = {
            "listAddress": listAddress,
            "get_country": get_country,
            "get_state": get_state,
        }

        # cases when the query, country and state not empty
        if query != '' and country != 'DEFAULT' and state != '':
            for y in get_state:
                z = y.lower()
                if strState in z:
                    for i in products:
                        print(i)
                        x = i.lower()
                        if strState in x:
                            if strCountry in x:
                                if strQuery in x:
                                    print("printing out the query: " + strQuery)
                                    print("Success!")
                                    listAddress.append((i))
            return render(request, 'searchAddress.html', context=context)

        # cases when the query is empy and country is set to default
        if query == '' and country == 'DEFAULT':
            for y in get_state:
                z = y.lower()
                if strState in z:
                    for i in products:
                        print(i)
                        x = i.lower()
                        if strState in x:
                            print("printing out the query: " + strQuery)
                            print("Success!")
                            listAddress.append((i))
            return render(request, 'searchAddress.html', context=context)

       # cases when the query is only empty
        if query == '':
            for i in products:
                print(i)
                x = i.lower()
                if strQuery in x:
                    print("testing the strquery condition")
                    if strCountry in x:
                        if strState in x:
                            print("printing out the query: " + strQuery)
                            print("Success!")
                            listAddress.append((i))
            print(country)
            print(listAddress)
            return render(request, 'searchAddress.html', context=context)

        # cases when country is default
        if country == "DEFAULT":
            # cases when state is empty but query is not
            if state == '' and query !='':
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
                return render(request,'searchAddress.html',context=context)

            #cases when state is not empty and query is
            if state != '' and query =='':
                for y in get_state:
                    z = y.lower()
                    if strState in z:
                        for i in products:
                            print(i)
                            x = i.lower()
                            if strState in x:
                                print("printing out the query: " + strQuery)
                                print("Success!")
                                listAddress.append((i))
                return render(request, 'searchAddress.html', context=context)

            #cases when both state and query is not empty
            if state != '' and query != '':
                for y in get_state:
                    z = y.lower()
                    if strState in z:
                        for i in products:
                            print(i)
                            x = i.lower()
                            if strState in x:
                                if strQuery in x:
                                    print("printing out the query: " + strQuery)
                                    print("Success!")
                                    listAddress.append((i))
                return render(request, 'searchAddress.html', context=context)

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
            return render(request,'searchAddress.html',context=context)
        else:
            print("No information to show")
            return request(request,'searchAddress.html',{})

