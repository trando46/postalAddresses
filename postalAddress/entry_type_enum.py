import enum
from django.utils.translation import gettext_lazy as _

"""
Enum class for form entry types. This is a required field in the CountryAddressFormat class that
holds a JSON string taken from the API to show how a country's address format is constructed,


Used in the JSON string pulled from the API  
Referenced in the format field of the address format model

Using text choice to be able to reference with Django
"""

class FormEntry(enum.Enum):
    DEFAULT = 0
    TEXT = 1
    DROPDOWN = 2
