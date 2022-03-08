from django.contrib import messages
from django.shortcuts import render
from myapi.models import Addresses
import json
from django.core import serializers
from myapi.models import CountryAddressStructure
from myapi.forms  import Addressesforms
def index(request):
    showall=Addresses.objects.all()
    showall1=Addresses.objects.values_list()
    
    countries=[]
    Id = Addresses.objects.values_list('country_id', flat=True)
    name = CountryAddressStructure.objects.values_list('country_name', flat=True)
    for i in range(0,len(Id)):
        countries.append(" "+name[Id[i]-1])
    #print(countries)
    showall1=list(showall1)
    result=[]
    for i in range(0,len(showall1)):
        t1=list(showall1[i][2].values())
        t1.append(countries[i])
        print(t1)
        result.append(t1)
        
    result=[''.join(ele) for ele in result]
    #print(result)
        
        
    return result
    #return render(request,'index.html',{"data":showall})]
    #a,one = CountryAddressStructure.objects.get("country_name").prefetch_related('relateds')
    

def read(request,address_id):
    readobj=Addresses.objects.get(address_id=address_id)
    #return list(readobj)
    return render(request,'index.html',{"data":readobj})

def create(request,model):
    saverecord=Addresses()
    saverecord.address_id=model[0]
    saverecord.country_ids=model[1]
    saverecord.addressLine=model[2]
    #print("done")
    saverecord.save()
    messages.success(request,'add  Is saved sucessfully.....!')
    
    return render(request,'insert.html')
    

def update(request,address_id):
    UpdateAdd=Addresses.objects.get(address_id=address_id)
    form=Addressessforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        #return 'Record Update Successfully....!'
        #return list(UpdateAdd)
        return render(request,'Edit.html',{"AddModel":UpdateAdd})

def Delete(request,address_id):
    delAddloyee=Addresses.objects.get(address_id=address_id)
    delAddloyee.delete()
    showdata=CountryTerritories.objects.all()
    #return "delete done"
    #return list(showdata)
    return render(request,'index.html',{"data": showdata})
   
