from django.contrib import admin
from .models import data_base ,Reg_base , Emergency_base

# Register your models here.
admin.site.register(data_base)
admin.site.register(Reg_base)
admin.site.register(Emergency_base)