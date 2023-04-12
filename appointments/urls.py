from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.createAppointment),
    path('update/',views.updateAppointment),
    path('delete/',views.deleteAppointment),
    path('lists/',views.listAllAppointment)
]