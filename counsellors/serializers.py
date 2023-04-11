from rest_framework import serializers
from .models import Counsellor

class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = '__all__'
