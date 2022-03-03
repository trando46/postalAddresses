from django.urls import path
from . import views

"""a placeholder file for the URLConf module for the myapi"""
urlpatterns = [
     # A view function that will be called if the URL pattern is detected: views.index,
    # which is the function named index() in the views.py file.
    path('', views.index, name='index'),
]