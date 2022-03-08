from django.contrib import messages
from django.shortcuts import render
from myapi.models import States
from myapi.models import Addresses
from myapi.forms import Statesforms
# it will take all the objects from index
def index(request):
    name = States.objects.values_list('state', flat=True)
    # print(list(showall1))
    print(list(name))
    return list(name)
    # it will take a particular index like a particular row or column
def read(request, state_id):
    readobj = States.objects.get(state_id=state_id)
    return list(readobj)
    #return render(request, 'Edit.html', {"State": readobj})
def create(request, model):
    saverecord = States()
    saverecord.state_id = model[0]
    saverecord.country_id = model[1]
    saverecord.state = model[2]

    # print("done")
    saverecord.save()
    messages.success(request, 'add Is saved sucessfully.....!')
    #return render(request, 'insert.html')
def update(request, state_id):
    UpdateAdd = States.objects.get(state_id=state_id)
    form = Statesforms(request.POST, instance=UpdateAdd)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully....!')
        return list(UpdateAdd)
        #return render(request, 'Edit.html', {"State": UpdateAdd})
# it will take particular id and delete it
def Delete(request, state_id):
    delAddloyee = States.objects.get(state_id=state_id)
    delAddloyee.delete()
    showdata = States.objects.all()
    return list(showdata)
    #return render(request, 'index1.html', {"data": showdata})
    # return "delete done"
