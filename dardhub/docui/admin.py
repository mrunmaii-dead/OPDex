from django.contrib import admin
from .models import Appointment , MedicineSchedule ,ScheduleTest,Tests
# Register your models here.
admin.site.register(Appointment)
admin.site.register(MedicineSchedule)
admin.site.register(ScheduleTest)
admin.site.register(Tests)