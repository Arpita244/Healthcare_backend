from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer, MappingSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid Credentials'}, status=400)
        
class RegisterView(generics.CreateAPIView):
    """
    API view to register a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    """
    API view to authenticate a user and return JWT tokens.
    """
    serializer_class = UserSerializer

    def post(self, request):
        """
        Handle POST request for user login.
        Returns JWT tokens if credentials are valid.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=400)
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid Credentials'}, status=400)

class PatientListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create patients for the authenticated user.
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return patients belonging to the current user.
        """
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Save the patient with the current user as owner.
        """
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a patient.
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if response.status_code == 404:
            response.data = {'error': 'Patient not found.'}
        return response
class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class DoctorListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create doctors.
    """
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all()

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a doctor.
    """
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all()

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if response.status_code == 404:
            response.data = {'error': 'Doctor not found.'}
        return response

class MappingListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create patient-doctor mappings.
    """
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

class MappingDetailView(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a patient-doctor mapping.
    """
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if response.status_code == 404:
            response.data = {'error': 'Mapping not found.'}
        return response

class PatientMappingsView(generics.ListAPIView):
    """
    API view to list all mappings for a specific patient.
    """
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return all mappings for the given patient ID.
        """
        patient_id = self.kwargs.get('patient_id')
        if not patient_id:
            raise serializers.ValidationError({'error': 'Patient ID is required.'})
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()

class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all()

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Doctor.objects.all()

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()

class MappingDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()

class PatientMappingsView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)
