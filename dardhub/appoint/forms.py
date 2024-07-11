from django import forms
from .models import data_base , Reg_base  , Emergency_base

from django.forms import inlineformset_factory
class InputForm(forms.ModelForm):
    class Meta:
        model = data_base
        
        fields =['name','doctor','complaint']

class RegForm(forms.ModelForm):
    class Meta:
        model = Reg_base
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'youremail@gmail.com'}),
            'height' :  forms.TextInput(attrs={'placeholder': 'height in cms'}),
            'weight' :  forms.NumberInput(attrs={'placeholder': '0'}),
            'password': forms.PasswordInput(),
        }
        fields = ['first_name' , 'last_name' , 'phone_number' ,'email','age','blood_group','gender','weight' , 'height','recognition_mark','allergen','password']

class EmerForm(forms.ModelForm):
   class Meta:
        model = Emergency_base
        fields = ['name' , 'relation','contact' , 'address']


#EmerSubForm = inlineformset_factory(Reg_base, data_base, form=EmerForm, extra=1)         