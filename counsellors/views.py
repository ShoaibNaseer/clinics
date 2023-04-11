from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Counsellor
from .serializers import CounsellorSerializer


@api_view(['POST'])
def createCounsellor(request):
    if not request.data['name'].replace(' ', '').isalpha():
        return Response({'error' : 'Name must be in alphabets'}, status=400)
    serializer = CounsellorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def updateCounsellor(request):
    email = request.data['email']
    id = request.data['id']
    if email:
        try:
            counsellor = Counsellor.objects.get(email=email)
            counsellor.is_active = True
        except:
            return Response({'error': 'Counsellor not found'}, status=404)
    if id:
        counsellor = Counsellor.objects.get(id=id)
    if id or email:
        serializer = CounsellorSerializer(counsellor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response({'error': 'Missing parameter'}, status=400)


@api_view(['DELETE'])
def deleteCounsellor(request):
    counsellor_email = request.query_params.get('email')
    id = request.query_params.get('id')
    if counsellor_email:
        try:
            counsellor = Counsellor.objects.get(email=counsellor_email)
        except:
            return Response({'error': 'Patient not found'}, status=404)
    if id:
        counsellor = Counsellor.objects.get(id=id)
    if counsellor_email or id:
        counsellor.is_active = False
        counsellor.save(update_fields=['is_active'])
        serializer = CounsellorSerializer(counsellor)
        return Response(serializer.data)
    return Response({'error': 'Missing parameter'}, status=400)


@api_view(['GET'])
def listAllCounsellor(request):
    is_active_counsellor = request.query_params.get('is_active')
    if is_active_counsellor == '1':
        counsellor = Counsellor.objects.filter(is_active=1)
        serializer = CounsellorSerializer(counsellor, many=True)
        return Response(serializer.data)
    return Response({'error': 'Invalid Params'}, status=404)
