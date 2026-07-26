from django.contrib import admin
from .models import Doctor, Patient, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
   list_display = (
      "id",
      "name",
      "specialization",
   )

   search_fields = (
      "name",
      "specialization",
   )

   list_filter = (
      "name",
   )

   ordering = (
      "name",
   )


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
   list_display =(
      "id",
      "name",
      "phone",
   )

   search_fields =(
      "name",
      "phone",
   )

   list_filter = (
      "name",
   )

   ordering = (
      "name",
   )



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
   list_display = (
      "id",
      "doctor",
      "patient",
      "appointment_date",
      "status",
   )

   list_filter = (
      "status",
      "doctor",
      "appointment_date",
   )

   search_fields = (
      "doctor_name",
      "patient_name",
   )

   ordering = (
      "-appointment_date",
   )

   autocomplete_fields = (
      "doctor",
      "patient",
   )

   list_per_page = 20


