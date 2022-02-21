import models
import requests
import repository


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

    def Create_State(self):
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