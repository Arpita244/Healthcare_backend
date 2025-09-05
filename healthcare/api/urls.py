"""
API URL patterns for the healthcare app.
Each endpoint is mapped to its corresponding view.
"""
from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingDetailView, PatientMappingsView
)

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

    # Patient endpoints
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Doctor endpoints
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Patient-Doctor Mapping endpoints
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),
    path('mappings/<int:patient_id>/', PatientMappingsView.as_view(), name='patient-mappings'),
]
from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingDetailView, PatientMappingsView
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),
    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),
    path('mappings/', MappingListCreateView.as_view()),
    path('mappings/<int:pk>/', MappingDetailView.as_view()),
    path('mappings/patient/<int:patient_id>/', PatientMappingsView.as_view()),
]
