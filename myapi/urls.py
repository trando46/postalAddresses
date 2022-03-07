from django.urls import path
from . import views
from postalAddress import CountryAddressStructureRepository
"""a placeholder file for the URLConf module for the myapi"""
urlpatterns = [
     # A view function that will be called if the URL pattern is detected: views.index,
    # which is the function named index() in the views.py file.
    path('', views.index, name='index'),
    path('show',CountryAddressStructureRepository.index1,name="show"),
    path('read/<int:country_id>',CountryAddressStructureRepository.read,name="read"),
    path('update/<int:country_id>',CountryAddressStructureRepository.update,name="update"),
    path('Delete/<int:country_id>',CountryAddressStructureRepository.Delete,name="Del"),
   
]
