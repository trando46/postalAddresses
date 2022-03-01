from django.contrib import messages
from django.shortcuts import render
from models import CountryTerritories
#it will take all the objects from index 
def index():
    showall=CountryTerritories.objects.all()
    return showall
    #it will take a particular index like a particular row or column
def read(id):
    readobj=CountryTerritories.objects.get(id=id)
    return readobj
    #it will take  input as a list and it will create objects
def create(model):
    saverecord=CountryTerritories()
    saverecord.states=model[0]
    saverecord.country=model[1]
    saverecord.country_iso=model[2]
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
#it will take particular id and delete it
def Delete(id):
    delAddloyee=CountryTerritories.objects.get(id=id)
    delAddloyee.delete()
    #showdata=CountryTerritories.objects.all()
    return "delete done"
   