from django.db import models

# Create your models here.

from django.utils import timezone

# Create your models here.

class data_base(models.Model):
    class choose(models.TextChoices):
     opd = 'OPD'
     ent = 'ENT' 
    class stat(models.TextChoices):
       pending = 'pending'
       done = 'done' 
    name = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100 , choices= choose.choices)
    complaint = models.CharField(max_length=50 )
    status = models.CharField(max_length=50 , choices= stat.choices , default= stat.pending)
def __str__(self):
        return self.name + ' ' + self.doctor    


class Reg_base(models.Model):
    #data_base = models.ForeignKey(data_base, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50 , null = True , blank = True)
    last_name = models.CharField(max_length=50 , null = True , blank = True)
    phone_number = models.IntegerField(default = 0)
    email = models.EmailField(null = True , blank = True)
    age = models.IntegerField(default=0)
    blood_group = models.CharField(max_length=3 , null = True , blank = True)
    gender = models.CharField(max_length=3 , null = True , blank = True)
    weight = models.IntegerField( default= 0)
    height = models.CharField(max_length=5 , null = True , blank = True)
    recognition_mark = models.CharField(max_length=200, default = "NA")
    allergen = models.CharField(max_length=200, default = "NA")
   
   


class Emergency_base(models.Model):

   name = models.CharField(max_length = 200 , null = True , blank = True)
   relation = models.CharField(max_length = 200 , null = True , blank = True)
   contact = models.CharField(max_length = 200 , null = True , blank = True)
   address = models.CharField(max_length = 200 , null = True , blank = True) #


   