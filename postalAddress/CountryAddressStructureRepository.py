from django.contrib import messages
from django.shortcuts import render
from myapi.models import CountryAddressStructure
from myapi.models import Addresses
from myapi.forms  import CountryAddressStructureforms 
#it will take all the objects from index

def index(request):
    #showall=CountryAddressStructure.objects.all()
    #showall1=CountryAddressStructure.objects.values_list()
    name = CountryAddressStructure.objects.values_list('country_name', flat=True)

    #print(list(showall1))
    
    return list(name)
    
    
    #it will take a particular index like a particular row or column
def index1(request):
    showall=CountryAddressStructure.objects.all()
    return render(request,'index1.html',{"data":showall})
    
    #it will take a particular index like a particular row or column
def read(request,country_id):
    readobj=CountryAddressStructure.objects.get(country_id=country_id)
    return list(readobj)
    #return render(request,'Edit.html',{"CountryAddressStructure":readobj})
def create(request,model):
    saverecord=CountryAddressStructure()
    saverecord.country_id=model[0]
    saverecord.country_name=model[1]
    saverecord.country_iso=model[2]
    saverecord.address_format=model[3]
    
    #print("done")
    saverecord.save()
    messages.success(request,'add Is saved sucessfully.....!')
    #return render(request,'insert.html')
    
    

def update(request,country_id):
    UpdateAdd=CountryAddressStructure.objects.get(country_id=country_id)
    form=CountryAddressStructureforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Update Successfully....!')
        return list(UpdateAdd)
        #return render(request,'Edit.html',{"CountryAddressStructure":UpdateAdd})
#it will take particular id and delete it
def Delete(request,country_id):
    delAddloyee=CountryAddressStructure.objects.get(country_id=country_id)
    delAddloyee.delete()
    showdata=CountryAddressStructure.objects.all()
    return list(showdata)
    #return render(request,'index1.html',{"data": showdata})
    #return "delete done"
 
