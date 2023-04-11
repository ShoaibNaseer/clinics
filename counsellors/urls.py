from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.createCounsellor),
    path('delete/',views.deleteCounsellor),
    path('update/',views.updateCounsellor),
    path('lists/',views.listAllCounsellor)
]