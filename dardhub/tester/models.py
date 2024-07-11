from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=100)

class MedicineNames(models.Model):
    name = models.CharField(max_length=100)
    medicine = models.ForeignKey(Medicine,related_name='medicine_names',on_delete=models.CASCADE)
    #medicne is foreign keu 