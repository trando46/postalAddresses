from django.contrib import messages
from django.shortcuts import render


def index(request):
    showall=Model.objects.all()
    return render(request,'index.html',{"data":showall})
def read(request,id):
    readobj=AddressModel.objects.get(id=id)
    return render(request,'index.html',{"data":readobj})

def create(request):
    if request.method =="POST":
        if request.POST.get('street') and request.POST.get('city') and
        request.POST.get('state') and request.POST.get('state_iso') and
        request.POST.get('country')and request.POST.get('country_iso') and
        request.POST.get('postal_code'):
            saverecord=AddressModel()
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
    EditAddobj=AddressModel.objects.get(id=id)
    return render(request,'Edit.html',{"AddModel":EditAddobj})

def update(request,id):
    UpdateAdd=AddressModel.objects.get(id=id)
    form=Addforms(request.POST,instance=UpdateAdd)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Update Successfully....!')
        return render(request,'Edit.html',{"AddModel":UpdateAdd})

def Delete(request,id):
    delAddloyee=AddressModel.objects.get(id=id)
    delAddloyee.delete()
    showdata=AddressModel.objects.all()
    return render(request,'index.html',{"data": showdata})
