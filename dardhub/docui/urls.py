from django.urls import path
from . import views
urlpatterns = [
    path("",views.appointments,name = "app page"),
    path("<int:pat_id>/",views.DocPage, name = "avtual fill"),
    path("<int:pat_id>/tests",views.Testorder, name = "tests"),
    path("<int:pat_id>/info" , views.InfoPage, name = "patient info")
]