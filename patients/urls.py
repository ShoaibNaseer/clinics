from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.createPatient),
    path('delete/',views.deletePatient),
    path('update/',views.updatePatient),
    path('lists/',views.listAllPatient)
]