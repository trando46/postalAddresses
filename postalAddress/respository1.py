from django.contrib import messages
from django.shortcuts import render
from models import AddressStructure

def index():
    showall=AddressStructure.objects.all()
    return showall

def read(id):
    readobj=AddressStructure.objects.get(id=id)
    return readobj

def create(model):
    saverecord=AddressStructure()
    saverecord.country_name=model[0]
    saverecord.country_iso=model[1]
    saverecord.address_format=model[2]
    #print("done")
    saverecord.save()
    return "sucess"
    

def update(request,id):
    UpdateAdd=CountryTerritories.objects.get(id=id)
    form=Addforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        return 'Record Update Successfully....!'
        #return render(request,'Edit.html',{"AddModel":UpdateAdd})

def Delete(id):
    delAddloyee=AddressStructure.objects.get(id=id)
    delAddloyee.delete()
    #showdata=CountryTerritories.objects.all()
    return "delete done"
   
