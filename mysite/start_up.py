from django.apps import AppConfig
from .models import address_format_model as afm
from .models import country_territories_model as ctm
from mysite.enums import entry_type_enum as ete

"""
This is the startup class to initialize our tables with default data and run processes
that are required on startup
"""


class AddressConfig(AppConfig):
    name = 'Postal Addresses'

    def ready(self):
        # query for the US address structure
        USA = afm.AddressStructure(country_name="United States",
                                   country_iso="US",
                                   address_format=[
                                       afm.FormatFields(field_type=ete.FormEntry.TEXT,
                                                        key="addressLine",
                                                        display_name="Address Line 1",
                                                        optional=False),
                                       afm.FormatFields(field_type=ete.FormEntry.TEXT,
                                                        key="addressLine2",
                                                        display_name="Address Line 2",
                                                        optional=True),
                                       afm.FormatFields(field_type=ete.FormEntry.TEXT,
                                                        key="city",
                                                        display_name="City",
                                                        optional=False),
                                       afm.FormatFields(field_type=ete.FormEntry.DROPDOWN,
                                                        key="state",
                                                        display_name="State",
                                                        optional=False),
                                       afm.FormatFields(field_type=ete.FormEntry.TEXT,
                                                        key="zip",
                                                        display_name="Zip Code",
                                                        optional=False),
                                   ])
        USA.save() #save this data
        # Create some states for us to reference
        WA = ctm.CountryTerritories(country=USA.country_name,
                                        country_iso=USA.country_iso,
                                        state="Washington")
        ME = ctm.CountryTerritories(country=USA.country_name,
                                        country_iso=USA.country_iso,
                                        state="Maine")
        ND = ctm.CountryTerritories(country=USA.country_name,
                                    country_iso=USA.country_iso,
                                    state="North Dakota")

        # query for the UK

        # query for the Canada

        # query for the Brazil

        # query for the Germany

        # query for the India

        # query for the Japan

        # query for the Korea

        # query for the Mexico

        # query for the Spain
