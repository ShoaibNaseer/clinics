from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/', include('patients.urls')),
    path('appointment/', include('appointments.urls')),
    path('counsellor/', include('counsellors.urls'))
]
