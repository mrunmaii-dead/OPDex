from django.urls import path

from . import views
urlpatterns = [
    path("",views.HomePage,name = "patient"),
    path("reg/",views.RegPage , name = "newreg"),
]