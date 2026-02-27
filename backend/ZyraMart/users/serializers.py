# serializers.py
from rest_framework import serializers
from .models import User


class AdminLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'is_vendor', 'profile_image']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # password hash করে save করবে
        user.save()
        return user
    



#     from django.core.validators import RegexValidator

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     phone_number = serializers.CharField(
#         required=True,
#         validators=[
#             RegexValidator(
#                 regex=r'^01[3-9]\d{8}$', 
#                 message="Phone number must be a valid Bangladeshi number"
#             )
#         ]
#     )

#     class Meta:
#         model = User
#         fields = [
#             'username', 'first_name', 'last_name', 'email',
#             'phone_number', 'password', 'profile_image'
#         ]

#     def create(self, validated_data):
#         validated_data['is_vendor'] = False  # normal user cannot be vendor
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)  # password hashed save
#         user.save()
#         return user