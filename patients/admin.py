from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email')

admin.site.register(Patient, PatientAdmin)

