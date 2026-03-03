# serializers.py
from rest_framework import serializers
from .models import User


# AdminLoginSerializer

class AdminLoginSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required = True)
    username = serializers.CharField(required = True)