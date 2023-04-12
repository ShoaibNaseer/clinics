from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Appointment
from patients.models import Patient
from counsellors.models import Counsellor
from .serializers import AppointmentSerializer, AppointmentSerializerList
from datetime import datetime


@api_view(['POST'])
def createAppointment(request):
    patient_email = request.data['patient_email']
    counsellor_email = request.data['counsellor_email']
    try:
        patient_id = Patient.objects.get(email=patient_email, is_active=1).id
        counsellor_id = Counsellor.objects.get(email=counsellor_email, is_active=1).id
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)
    except Counsellor.DoesNotExist:
        return Response({'error': 'Counsellor not found'}, status=404)
    try:
        appointment_date = datetime.strptime(request.data['appointment_date'], "%Y-%m-%d %H:%M:%S")
        if datetime.now() > appointment_date:
            return Response({'error': 'Date cant be in past'}, status=404)
    except:
        return Response({'error': 'Date has invalid format. It must be yyyy-m-d h:m:s'}, status=404)
    is_appointment = Appointment.objects.filter(patient_id=patient_id, counsellor_id=counsellor_id, appointment_date=appointment_date)
    if is_appointment:
        return Response({'error': 'Patient and Counsellor has already an appointment on particular date'}, status=404)
    data = {
        'patient_id': patient_id,
        'counsellor_id': counsellor_id,
        'appointment_date': appointment_date,
        'is_active': True
    }
    serializer = AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateAppointment(request):
    patient_email = request.data['patient_email']
    counsellor_email = request.data['counsellor_email']
    try:
        patient_id = Patient.objects.get(email=patient_email).id
        counsellor_id = Counsellor.objects.get(email=counsellor_email).id
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)
    except Counsellor.DoesNotExist:
        return Response({'error': 'Counsellor not found'}, status=404)
    try:
        appointment_date = datetime.strptime(request.data['appointment_date'], "%Y-%m-%d %H:%M:%S")
        if datetime.now() > appointment_date:
            return Response({'error': 'Date cant be in past'}, status=404)
    except:
        return Response({'error': 'Date has invalid format. It must be yyyy-m-d h:m:s'}, status=404)
    is_appointment = Appointment.objects.filter(patient_id=patient_id, counsellor_id=counsellor_id, appointment_date=appointment_date)
    if is_appointment:
        return Response({'error': 'Patient and Counsellor has already an appointment on particular date'}, status=404)
    data = {
        'patient_id': patient_id,
        'counsellor_id': counsellor_id,
        'appointment_date': appointment_date,
        'is_active': True
    }
    serializer = AppointmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteAppointment(request):
    id = request.query_params.get('id')
    if id:
        try:
            appointment = Appointment.objects.get(id=id)
        except:
            return Response({'error': 'Appointment not found'}, status=404)
        appointment.is_active = False
        appointment.save(update_fields=['is_active'])
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    return Response({'error': 'Missing parameter'}, status=400)


@api_view(['DELETE'])
def deleteCounsellor(request):
    appointment_id = request.query_params.get('appointment_id')
    if appointment_id:
        try:
            appointment = Appointment.objects.get(id=appointment_id)
        except:
            return Response({'error': 'Appointment not found'}, status=404)
        appointment.is_active = False
        appointment.save(update_fields=['is_active'])
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    return Response({'error': 'Missing email parameter'}, status=400)


@api_view(['GET'])
def listAllAppointment(request):
    is_active_params = request.query_params.get('is_active')
    is_patient = request.query_params.get('patient')
    is_counsellor = request.query_params.get('counsellor')
    is_date_from = request.query_params.get('date_from')
    is_date_to = request.query_params.get('date_to')
    if is_active_params:
        patients = Appointment.objects.filter(is_active=1)
        serializer = AppointmentSerializerList(patients, many=True)
        return Response(serializer.data)
    if is_patient:
        try:
            patient_id = Patient.objects.get(email=is_patient).id
        except:
            return Response({'error': 'Patient not found'}, status=404)
        patients = Appointment.objects.filter(patient_id=patient_id)
        serializer = AppointmentSerializerList(patients, many=True)
        return Response(serializer.data)
    if is_counsellor:
        try:
            counsellor_id = Counsellor.objects.get(email=is_counsellor).id
        except:
            return Response({'error': 'Counsellor not found'}, status=404)
        patients = Appointment.objects.filter(counsellor_id=counsellor_id)
        serializer = AppointmentSerializerList(patients, many=True)
        return Response(serializer.data)
    if is_date_from and is_date_to:
        start_date = datetime.strptime(is_date_from, "%Y-%m-%d").date()
        end_date = datetime.strptime(is_date_to, "%Y-%m-%d").date()
        appointment = Appointment.objects.filter(appointment_date__range=[start_date, end_date], is_active=1).order_by(
            'appointment_date')
        serializer = AppointmentSerializerList(appointment, many=True)
        return Response(serializer.data)
    return Response({'error': 'Invalid Params'}, status=404)
