from .models import Appointment , MedicineSchedule
from django import forms
from django.forms import inlineformset_factory
class docform(forms.ModelForm):
       class Meta:
        model = Appointment
        widgets = {
            #'refer_back': forms.DateInput(attrs={'type': 'date'}),
             #'complaint': forms.Textarea(),
             'doctors_assessment': forms.Textarea(attrs={'placeholder': 'Doctors Assessment'}),
            
            
        }
        fields =['complaint','doctors_assesment','refer_back',]
class MedicineScheduleForm(forms.ModelForm):
    class Meta:
        model = MedicineSchedule
        fields = ['medicine_name', 'morning', 'afternoon', 'evening', 'night', 'dose', 'duration']

MedicineScheduleFormSet = inlineformset_factory(Appointment, MedicineSchedule, form=MedicineScheduleForm, extra=1)    