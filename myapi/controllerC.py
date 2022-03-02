from django.contrib import messages
from django.shortcuts import render
from myapi import repository

def index(request):
    return repository.index(request)
"""def read(request,id):
    readobj=AddressModel.objects.get(id=id)
    return render(request,'index.html',{"data":readobj})
"""
def create(request):
    l=[]
    #print("hi1")
    if request.method =="POST":
        #print("h2")
        if request.POST.get('country_id') and request.POST.get('country_name')and request.POST.get('country_iso') and request.POST.get('address_format'):
            l.append(request.POST.get('country_id'))
            l.append(request.POST.get('country_name'))
            l.append(request.POST.get('country_iso'))
            l.append(request.POST.get('address_format'))
            return repository.create(request,l)            
    else:
        return render(request,'insert.html')
