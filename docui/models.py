from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Appointment(models.Model):
    
    class choose(models.TextChoices):
        before = 'before meal'
        after = 'after meal'
    class Ref(models.TextChoices):
        yes = 'yes'
        no = 'no'
    complaint = models.CharField(max_length=200)
    doctors_assesment = models.CharField(max_length=200)
    
    refer_back = models.CharField(max_length=100 , choices = Ref.choices , default=Ref.no)
    
    def __str__(self) :
        return self.complaint + self.doctors_assesment
    
class MedicineSchedule(models.Model):
    class choose(models.TextChoices):
        before = 'before'
        after = 'after'

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)
    evening = models.BooleanField(default=False)
    night = models.BooleanField(default=False)
    dose = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField(default=1)
    bef = models.BooleanField(default=False)
    aft = models.BooleanField(default=False)
 #need foreignkey to ensure i can use nested forms
