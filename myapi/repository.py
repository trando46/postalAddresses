from django.contrib import messages
from django.shortcuts import render
from myapi.models import CountryAddressStructure
#it will take all the objects from index 
def index(request):
    showall=CountryAddressStructure.objects.all()
    return render(request,'index.html',{"data":showall})
    
    #it will take a particular index like a particular row or column
def read(request,id):
    readobj=CountryAddressStructure.objects.get(country_id=id)
    return render(request,'index.html',{"data":readobj})
    #it will take  input as a list and it will create objects
def create(request,model):
    saverecord=CountryAddressStructure()
    saverecord.country_id=model[0]
    saverecord.country_name=model[1]
    saverecord.country_iso=model[2]
    saverecord.address_format=model[3]
    
    #print("done")
    saverecord.save()
    messages.success(request,'add Is saved sucessfully.....!')
    return render(request,'insert.html')
    
    

def update(request,id):
    UpdateAdd=CountryAddressStructure.objects.get(country_id=id)
    form=Addforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        #return 'Record Update Successfully....!'
        return render(request,'Edit.html',{"AddModel":UpdateAdd})
#it will take particular id and delete it
def Delete(request,id):
    delAddloyee=CountryAddressStructure.objects.get(id=id)
    delAddloyee.delete()
    showdata=CountryTerritories.objects.all()
    return render(request,'index.html',{"data": showdata})
    #return "delete done"
   
