from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.createAppointment),
    path('lists/',views.listAllAppointment)
]