from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from appoint.models import data_base ,Reg_base
# Create your views here.
from django.shortcuts import render,get_object_or_404
from .forms import docform,MedicineScheduleFormSet
from django.http import HttpResponse
from .models import Appointment

def DocPage(request,pat_id):
   
    profile = data_base.objects.all()
    if request.method == 'POST':
        form = docform(request.POST)
        formset = MedicineScheduleFormSet(request.POST, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            app = form.save()
            formset.instance = app
            formset.save()
            return redirect('/doctor')  # Redirect to a success page
    else:
        form = docform()
        formset = MedicineScheduleFormSet(instance=form.instance)
    context = {
        "form" : form,
        "profiles" : profile,
        "pat_id" : pat_id,
        'formset':formset

     }
    return render(request, 'doctor.html', context)

def appointments(request):
   # return HttpResponse("you are looking at patirtne %s" % pat_id)
   profile = data_base.objects.all().order_by('-id')
   context = {
    
        "profiles" : profile

     }
   return render(request, 'apps.html', context)

def Changestatus(request,pat_id):
     item = get_object_or_404(data_base , pk = pat_id)
     if item.status == 'pending':
        item.status = 'done'
        item.save()
def Testorder(request , pat_id):
    return HttpResponse("here you'll order tests")
def InfoPage(request , pat_id):
    pat_nameid = data_base.objects.get(id = pat_id)
    pat_name = Reg_base.objects.filter(first_name = pat_nameid.name)
    information = Reg_base.objects.all()

    
    context = {
        "inf": information,
        "pat_id" : pat_id,
        "pat_name" : pat_name,
    }

    return render(request, 'info.html', context)
     

    