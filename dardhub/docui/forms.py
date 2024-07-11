from .models import Appointment , MedicineSchedule , ScheduleTest ,Tests
from django import forms
from django.forms import inlineformset_factory
class docform(forms.ModelForm):
       class Meta:
        model = Appointment
        widgets = {
            #'refer_back': forms.DateInput(attrs={'type': 'date'}),
             #'complaint': forms.Textarea(),
             'doctors_assessment': forms.Textarea(attrs={'placeholder': 'Doctors Assessment'}),
             'refer_back_date': forms.DateInput(attrs={'type': 'date'}),
            
            
        }
        fields =['complaint','doctors_assesment','refer_back','refer_back_date']
class MedicineScheduleForm(forms.ModelForm):
    class Meta:
        model = MedicineSchedule
        fields = ['medicine_name', 'morning', 'afternoon', 'evening', 'night', 'dose', 'duration','bef','aft']

MedicineScheduleFormSet = inlineformset_factory(Appointment, MedicineSchedule, form=MedicineScheduleForm, extra=5)    

class TestForm(forms.ModelForm):
    class Meta:
        model = ScheduleTest
        widgets = {
            'date_to_be_done': forms.DateInput(attrs={'type': 'date'}),
        }
        fields = [ 'test_name','date_to_be_done','additional_notes']
class TestsForm(forms.ModelForm):
    class Meta:
        model = Tests
        fields = ['patient_name']        