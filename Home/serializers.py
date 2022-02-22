# serializers.py
from rest_framework import serializers
from .models import USERdata


class simpleModelserilizer(serializers.ModelSerializer):
    
    class Meta:
        model = USERdata
        fields = '__all__'
