from postalAddress.models import models
import repository
from django.contrib import messages
from django.shortcuts import HttpResponse, render, redirect

class Controller:


    # I think the flow is like this,
    '''
    1. API Controller handles POST GET methods and send request to repository
    2. Repository Communicates to the Database and returns appropriate values to API controller.
    '''

    def __init__(self):
        pass

    def Address_Controller(self, request):
        if request.method == "POST":
            self.street = "" if not (request.POST.get('street')) else str(request.POST.get('street'))
            self.city = "" if not (request.POST.get('city')) else str(request.POST.get('city'))
            self.state = "" if not (request.POST.get('state')) else str(request.POST.get('state'))
            self.state_iso = "" if not (request.POST.get('state_iso')) else str(request.POST.get('state_iso'))
            self.country = "" if not (request.POST.get('country')) else str(request.POST.get('country'))
            self.country_iso = "" if not (request.POST.get('country_iso')) else str(request.POST.get('country_iso'))
            self.postal_code = "" if not (request.POST.get('postal_code')) else str(request.POST.get('postal_code'))


        elif request.method == "Get":
            pass

    def Process_Repository_Errors(self, request, Error_Code):
        if Error_Code == 200:
            return messages.info(request, "Request Successful..")
        elif Error_Code == 201:
            return messages.error(request, "Request failed..")
        elif Error_Code == 404:
            return messages.error(request, "Not Found..")

        #Add state functionality
    def Create_State(self, request):
        if request.method == "POST":
            try:
                self.state = str(request.POST.get('state'))
                if len(self.state) <= 100 and len(self.state) >= 1: #validating
                    return self.Process_Repository_Errors(self.repository.create_state(self.state)) #this will be a 200 or 201 errors
                else:
                    messages.error(request, "State Length should not be empty and should not be more than 100 characters ")
            except Exception as e:
                messages.error(request, "Creating State request was failed with an error - %s"%(str(e)))
                return redirect('Create_New_State')
        else:
            messages.error(request, "This should be a POST method, request declined.")

        if self.state not in self.Get_States():
            repository.create(self.country, self.state)

    def Get_States(self):
        states = repository.read(self.country)
        if states is not None:
            return states  # need to format

    def Get_cities(self):
        cities = repository.read(self.state)
        if cities is not None:
            return cities  # need to format