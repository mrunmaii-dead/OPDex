from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import InputForm , RegForm , EmerForm
from django.http import HttpResponse

def HomePage(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')  # Redirect to a success page
    else:
        form = InputForm()

    return render(request, 'home.html', {'form': form})
def RegPage(request):
      age_range = range(1, 101)
      if request.method == 'POST':
        form = RegForm(request.POST)
        form2 = EmerForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponse('success')  # Redirect to a success page
      else:
        form = RegForm()
        form2 = EmerForm()

      return render(request, 'reg.html', {'form': form , 'form2' : form2,'age_range':age_range })