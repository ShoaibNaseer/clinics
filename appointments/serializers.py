from rest_framework import serializers
from .models import Appointment
from patients.models import Patient
from counsellors.models import Counsellor

# class PatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient
#         fields = ('id', 'name')
#
# class CounsellorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Counsellor
#         fields = ('id', 'name')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentSerializerList(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient_id.name')
    counsellor_name = serializers.CharField(source='counsellor_id.name')

    class Meta:
        model = Appointment
        fields = ('id', 'appointment_date', 'is_active', 'patient_name', 'counsellor_name')


