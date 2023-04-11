from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_patient_name', 'get_counsellor_name', 'appointment_date')
    search_fields = ('id', 'patient__name', 'counsellor__name', 'appointment_date')

    def get_patient_name(self, obj):
        return obj.patient_id.name

    def get_counsellor_name(self, obj):
        return obj.counsellor_id.name

    get_patient_name.short_description = 'Patient Name'
    get_counsellor_name.short_description = 'Counsellor Name'


admin.site.register(Appointment, AppointmentAdmin)
