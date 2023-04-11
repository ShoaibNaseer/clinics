from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Patient
from .serializers import PatientSerializer


@api_view(['POST'])
def createPatient(request):
    if not request.data['name'].replace(' ', '').isalpha():
        return Response({'error' : 'Name must be in alphabets'}, status=400)
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updatePatient(request):
    email = request.data['email']
    if email:
        try:
            patient = Patient.objects.get(email=email)
            patient.is_active = True
        except:
            return Response({'error': 'Patient not found'}, status=404)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response({'error': 'Missing email parameter'}, status=400)


@api_view(['DELETE'])
def deletePatient(request):
    patient_email = request.query_params.get('email')
    id = request.query_params.get('id')
    if patient_email:
        try:
            patient = Patient.objects.get(email=patient_email)
        except:
            return Response({'error': 'Patient not found'}, status=404)
    if id:
        patient = Patient.objects.get(id=id)
    if id or patient_email:
        patient.is_active = False
        patient.save(update_fields=['is_active'])
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    return Response({'error': 'Missing email parameter'}, status=400)


@api_view(['GET'])
def listAllPatient(request):
    is_active_patient = request.query_params.get('is_active')
    if is_active_patient == '1':
        patients = Patient.objects.filter(is_active=1)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    return Response({'error': 'Invalid Params'}, status=404)
