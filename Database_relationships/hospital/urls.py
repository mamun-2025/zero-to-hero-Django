

from django.urls import path
from . import views

app_name = "hospital"

urlpatterns = [
   path("doctors/", views.doctor_list, name="doctor_list"),
   path("doctors/<int:pk>/", views.doctor_detail, name="doctor_detail"),
   path("doctors/create/", views.doctor_create, name="doctor_create"),
   path("doctors/<int:pk>/update/", views.doctor_update, name="doctor_update"),
   path("doctors/<int:pk>/delete/", views.doctor_delete, name="doctor_delete"),

   path("patient/", views.patient_list, name="patient_list"),
   path("patient/<int:pk>/", views.patient_detail, name="patient_detail"),
   path("patient/create/", views.patient_create, name="patient_create"),
   path("patient/<int:pk>/update", views.patient_update, name="patient_update"),
   path("patient/<int:pk>/delete", views.patient_delete, name="patient_delete"),

   
   path("appointment/", views.appointment_list, name="appointment_list"),
   path("appointment/<int:pk>/", views.appointment_detail, name="appointment_detail"),
   path("appointment/create/", views.appointment_create, name="appointment_create"),
   path("appointment/<int:pk>/update", views.appointment_update, name="appointment_update"),
   path("appointment/<int:pk>/delete", views.appointment_delete, name="appointment_delete"),
    
]
