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
