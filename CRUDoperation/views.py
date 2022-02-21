from calendar import c
import importlib 
from django.shortcuts import render
from CRUDoperation.models import crudst
from django.contrib import messages
from CRUDoperation.forms import stform

#from django.views.decorators.csrf import csrf_exempt


def stdisplay(request):
    results = crudst.objects.all()
    return render(request, "index.html", {"crudst": results})

def stinsert(request):       
    print("inside stinsert", request.method)
    if request.method == "POST":
        print("inside stinsert 2nd", request.method)
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            print("I'm here : ", request.POST.get('stname'), request.POST.get('stemail'), request.POST.get(
                'staddress'), request.POST.get('stmobile'), request.POST.get('stgender'))
            savest = crudst()
            savest.stname = request.POST.get('stname')
            savest.stemail = request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.stgender = request.POST.get('stgender')
            savest.save()
            messages.success(request, "The record Is saved successfully..!")
            return render(request, "create.html")
    else:
        return render(request, "create.html")

def stedit(request, id):
    getstudentdetails = crudst.objects.get(id=id)
    return render(request, "edit.html", {"crudst": getstudentdetails})

def stupdate(request, id):
    stupdate = crudst.objects.get(id=id)
    form = stform(request.POST, instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request, "The student record is updated successfully")
        return render(request, "edit.html", {"crust": stupdate})


def stdel(request, id):
    delstudent = crudst.objects.get(id=id)
    delstudent.delete()
    results = crudst.objects.all()
    return render(request, "edit.html", {"crudst": results})
