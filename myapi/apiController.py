from django.contrib import messages
from django.shortcuts import render
from postalAddress import CountryAddressStructureRepository
from postalAddress import AddressesRespository
from postalAddress import StateRespository
from django.http import HttpResponseBadRequest

class Controller:


    def Get_States(request):
        #request is sent to the repository to get the list
        return StateRespository.index(request)

    def Add_States(request):
        #list for adding states
        states = []

        if request.method =="POST":
            #gets all the required parameters
            if request.POST.get('state_id') and request.POST.get('country_id')and request.POST.get('state') :
                # checks if there is input in each parameter
                if (len(request.POST.get('state_id'))) >=1:
                    states.append(request.POST.get('state_id'))
                else:
                    messages.error(request,'Enter valid state ID')
                    #return render(request,'insert.html')

                if (len(request.POST.get('country_id'))) >=1:
                    states.append(request.POST.get('country_id'))
                else:
                    messages.error(request,'Enter valid Country ID')
                    #return render(request,'insert.html')

                if (len(request.POST.get('state'))) >=1:
                    states.append(request.POST.get('state'))
                else:
                    messages.error(request,'Enter valid state')
                    #return render(request,'insert.html')
                # request is sent to the repository to create a new state
                return StateRespository.create(request,states)
        else:
            return HttpResponseBadRequest("We cannot process the request")

#get for country
    def Get_Country(request):
        # request is sent to the repository to get the list
        return CountryAddressStructureRepository.index(request)

#post for country
    def Add_Country(request):
        #list for adding CountryAddressFormat
        country=[]

        if request.method =="POST":
            # gets all the required parameters
            if request.POST.get('country_id') and request.POST.get('country_name')and request.POST.get('country_iso') and request.POST.get('address_format'):
                # checks if there is input in each parameter
                if (len(request.POST.get('country_id'))) >=1:
                    country.append(request.POST.get('country_id'))
                else:
                    messages.error(request,'Enter valid Country ID')
                    #return render(request,'insert.html')

                if (len(request.POST.get('country_name'))) >=1:
                    country.append(request.POST.get('country_name'))
                else:
                    messages.error(request,'Enter valid Country name')
                    #return render(request,'insert.html')

                if (len(request.POST.get('country_iso'))) >=1:
                    country.append(request.POST.get('country_iso'))
                else:
                    messages.error(request,'Enter valid Country ISO')
                    #return render(request,'insert.html')

                if (len(request.POST.get('address_format'))) >=1:
                    country.append(request.POST.get('address_format'))
                else:
                    messages.error(request,'Enter valid Address format')
                    #return render(request,'insert.html')
                    # request is sent to the repository to create a new country
                return CountryAddressStructureRepository.create(request,country)
        else:
            return HttpResponseBadRequest("We cannot process the request")

#get for Address
    def Get_Address(request):
        # request is sent to the repository to get the list
        return AddressesRespository.index(request)

#post for Address
    def Add_Address(request):
        #list for adding Address
        address = []

        if request.method =="POST":
            # gets all the required parameters
            if request.POST.get('address_id') and request.POST.get('country_id')and request.POST.get('addressLine') :
                #checks if there is input in each parameter
                if (len(request.POST.get('address_id'))) >=1:
                    address.append(request.POST.get('address_id'))
                else:
                    messages.error(request,'Enter valid Address ID')
                    #return render(request,'insert.html')

                if (len(request.POST.get('country_id'))) >=1:
                    address.append(request.POST.get('country_id'))
                else:
                    messages.error(request,'Enter valid Country ID')
                    #return render(request,'insert.html')

                if (len(request.POST.get('addressLine'))) >=1:
                    address.append(request.POST.get('addressLine'))
                else:
                    messages.error(request,'Enter valid Address Line')
                    #return render(request,'insert.html')
                # request is sent to the repository to create a new address
                return AddressesRespository.create(request,address)
        else:
            return HttpResponseBadRequest("We cannot process the request")


