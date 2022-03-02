from django.contrib import messages
from django.shortcuts import render
from myapi.models import Addresses

def index(request):
    showall=Addresses.objects.all()
    return render(request,'index.html',{"data":showall})
    #return showall

def read(request,id):
    readobj=Addresses.objects.get(id=id)
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
    

def update(request,id):
    UpdateAdd=Addresses.objects.get(id=id)
    form=Addforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        #return 'Record Update Successfully....!'
        return render(request,'Edit.html',{"AddModel":UpdateAdd})

def Delete(request,id):
    delAddloyee=Addresses.objects.get(id=id)
    delAddloyee.delete()
    showdata=CountryTerritories.objects.all()
    #return "delete done"
    return render(request,'index.html',{"data": showdata})
   
