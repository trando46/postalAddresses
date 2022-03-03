from django.contrib import messages
from django.shortcuts import render
from myapi import repository
from postalAddress import respository1

class Controller:

#get for country
    def Get_Country(request):
        return repository.index(request)

#post for country
    def Add_Country(request):
        #list for adding CountryAddressFormat
        country=[]

        if request.method =="POST":

            if request.POST.get('country_id') and request.POST.get('country_name')and request.POST.get('country_iso') and request.POST.get('address_format'):
                if (len(request.POST.get('country_id'))) >=1:
                    country.append(request.POST.get('country_id'))
                else:
                    messages.error(request,'Enter valid Country ID')
                    return render(request,'insert.html')

                if (len(request.POST.get('country_name'))) >=1:
                    country.append(request.POST.get('country_name'))
                else:
                    messages.error(request,'Enter valid Country name')
                    return render(request,'insert.html')

                if (len(request.POST.get('country_iso'))) >=1:
                    country.append(request.POST.get('country_iso'))
                else:
                    messages.error(request,'Enter valid Country ISO')
                    return render(request,'insert.html')

                if (len(request.POST.get('address_format'))) >=1:
                    country.append(request.POST.get('address_format'))
                else:
                    messages.error(request,'Enter valid Address format')
                    return render(request,'insert.html')

                return repository.create(request,country)
        else:
            return render(request,'insert.html')

#get for Address
    def Get_Address(request):
        return respository1.index(request)

#post for Address
    def Add_Address(request):
        #list for adding Address
        address = []

        if request.method =="POST":

            if request.POST.get('address_id') and request.POST.get('country_id')and request.POST.get('addressLine') :

                if (len(request.POST.get('address_id'))) >=1:
                    address.append(request.POST.get('address_id'))
                else:
                    messages.error(request,'Enter valid Address ID')
                    return render(request,'insert.html')

                if (len(request.POST.get('country_id'))) >=1:
                    address.append(request.POST.get('country_id'))
                else:
                    messages.error(request,'Enter valid Country ID')
                    return render(request,'insert.html')

                if (len(request.POST.get('addressLine'))) >=1:
                    address.append(request.POST.get('addressLine'))
                else:
                    messages.error(request,'Enter valid Address Line')
                    return render(request,'insert.html')

                return respository1.create(request,address)
        else:
            return render(request,'insert.html')


