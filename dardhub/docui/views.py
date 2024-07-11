from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect
from appoint.models import data_base ,Reg_base
# Create your views here.
from django.shortcuts import render,get_object_or_404
from .forms import docform,MedicineScheduleFormSet , TestForm,TestsForm
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
   if request.method == "POST":
        tests_form =TestsForm(request.POST)
        test_forms = [TestForm(request.POST, prefix=f'form_{i}') for i in range(5)]
        
        if tests_form.is_valid() and all(form.is_valid() for form in test_forms):
            tests_instance = tests_form.save()  # Save the parent Tests instance
            
            for form in test_forms:
                test_instance = form.save(commit=False)
                test_instance.tests = tests_instance  # Link each Test instance to the Tests parent
                test_instance.save()
            
            return HttpResponse('success')  # Redirect to a success URL or handle as needed
        
        # Handle what to do if forms are not valid
   else:
        tests_form = TestsForm()
        test_forms = [TestForm(prefix=f'form_{i}') for i in range(5)]
    
   context = {
        "tests_form": tests_form,
        "test_forms": test_forms,
    }
    
   return render(request, 'ordertest.html', context)      
def InfoPage(request , pat_id):
    pat_nameid = get_object_or_404(data_base, id=pat_id)
    pat_name = get_object_or_404(Reg_base, first_name__iexact=pat_nameid.name)
    information = Reg_base.objects.all()

    
    context = {
        "inf": information,
        "pat_id" : pat_id,
        "pat_name" : pat_name,
    }

    return render(request, 'info.html', context)
     

    