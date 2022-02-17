from django import forms
from django.shortcuts import render
from mysite.models import AddModel
from django.contrib import messages
from mysite.forms import Addforms
def index(request):
    showall=Model.objects.all()
    return render(request,'index.html',{"data":showall})
def read(request,id):
    readobj=AddModel.objects.get(id=id)
    return render(request,'index.html',{"data":readobj})

def create(request):
    if request.method =="POST":
        if request.POST.get('street') and request.POST.get('city') and
        request.POST.get('state') and request.POST.get('state_iso') and
        request.POST.get('country')and request.POST.get('country_iso') and
        request.POST.get('postal_code'):
            saverecord=AddModel()
            saverecord.street=request.POST.get('street')
            saverecord.city=request.POST.get('city')
            saverecord.state=request.POST.get('state')
            saverecord.state_iso=rrequest.POST.get('state_iso')
            saverecord.country=request.POST.get('country')
            saverecord.country_iso=request.POST.get('country_iso')
            saverecord.postal_code=request.POST.get('postal_code')
            saverecord.save()
            messages.success(request,'add' +saverecord.street+ ' Is saved sucessfully.....!')
        return render(request,'insert.html')
    else:
        return render(request,'insert.html')

def EditAdd(request,id):
    EditAddobj=AddModel.objects.get(id=id)
    return render(request,'Edit.html',{"AddModel":EditAddobj})
    
def update(request,id):
    UpdateAdd=AddModel.objects.get(id=id)
    form=Addforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Update Successfully....!')
        return render(request,'Edit.html',{"AddModel":UpdateAdd})

def Delete(request,id):
    delAddloyee=AddModel.objects.get(id=id)
    delAddloyee.delete()
    showdata=AddModel.objects.all()
    return render(request,'index.html',{"data": showdata})
