from django.shortcuts import render

# Create your views here.
# Structure this in a way where UI for the user 
# build our page base off of our model.py 
# Call the json and how are we going to pull it base on the display name 
# Step 1: Have a drop down of countries for the user to select, once the user select 
# Step 2: You have to build a form base on what country the user select 
# look at the models base on the formatFields we either createa text entry for the user or a drop down menu 
# and show the correct display names as well (self.display EX// state, addressline1, addressline2, zipcode)
# read the database, the first column would be something like the address structure and read the formatfields and populate that
# to the user 
# Step 3: html -> should dynamically populate the fields base on the json parsing of the database. 
# Google creating a dynamic form with Django 
# EX// selecting US -> populate 5 text entries and one of them have to be a drop down 