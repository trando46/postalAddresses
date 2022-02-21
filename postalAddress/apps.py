from django.apps import AppConfig
import models


class PostaladdressConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'postalAddress'

    def ready(self):
        # query for the US address structure
        USA = models.AddressStructure(country_name="United States",
                                      country_iso="US",
                                      address_format=[
                                          models.FormatFields(type=models.FormEntry.TEXT,
                                                              key="addressLine",
                                                              display="Address Line 1",
                                                              optional=False),
                                          models.FormatFields(type=models.FormEntry.TEXT,
                                                              key="addressLine2",
                                                              display="Address Line 2",
                                                              optional=True),
                                          models.FormatFields(type=models.FormEntry.TEXT,
                                                              key="city",
                                                              display="City",
                                                              optional=False),
                                          models.FormatFields(type=models.FormEntry.DROPDOWN,
                                                              key="state",
                                                              display="State",
                                                              optional=False),
                                          models.FormatFields(type=models.FormEntry.TEXT,
                                                              key="zip",
                                                              display="Zip Code",
                                                              optional=False),
                                      ])
        USA.save()  # save this data
        # Create some states for us to reference
        WA = models.CountryTerritories(country=USA.country_name,
                                       country_iso=USA.country_iso,
                                       state="Washington")
        WA.save()

        ME = models.CountryTerritories(country=USA.country_name,
                                       country_iso=USA.country_iso,
                                       state="Maine")
        ME.save()

        ND = models.CountryTerritories(country=USA.country_name,
                                       country_iso=USA.country_iso,
                                       state="North Dakota")
        ND.save()

        # query for the UK

        # query for the Canada

        # query for the Brazil

        # query for the Germany

        # query for the India

        # query for the Japan

        # query for the Korea

        # query for the Mexico

        # query for the Spain
