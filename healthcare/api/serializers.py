
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping

class UserSerializer(serializers.ModelSerializer):
    def validate_username(self, value):
        """
        Ensure the username is unique.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def validate_email(self, value):
        """
        Ensure the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    """
    Serializer for Django's built-in User model.
    Handles user creation with password hashing.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        """
        Create a new user with a hashed password.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class PatientSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Ensure all required fields are present.
        """
        required_fields = ['name', 'age', 'gender']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field.capitalize()} is required."})
        return data
    """
    Serializer for the Patient model.
    """
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Ensure all required fields are present and name is unique.
        """
        required_fields = ['name', 'specialization', 'contact_info']
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field.replace('_', ' ').capitalize()} is required."})
        # Unique name check
        if Doctor.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError({'name': "A doctor with this name already exists."})
        return data
    """
    Serializer for the Doctor model.
    """
    class Meta:
        model = Doctor
        fields = '__all__'

class MappingSerializer(serializers.ModelSerializer):
    """
    Serializer for the PatientDoctorMapping model.
    """
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
