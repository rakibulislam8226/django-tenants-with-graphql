from rest_framework import serializers
from .models import SweetType
class SweetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SweetType
        fields = '__all__'