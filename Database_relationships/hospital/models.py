from django.db import models


class Doctor(models.Model):

   name = models.CharField(max_length=100)
   specialization = models.CharField(max_length=100)

   def __str__(self):
      return self.name 



class Patient(models.Model):

   name = models.CharField(max_length=100)
   phone = models.CharField(max_length=20)

   def __str__(self):
      return self.name 



class Appointment(models.Model):

   class Status(models.TextChoices):
      PENDING = "Pending", "Pending"
      COMPLETED = "Completed", "Completed"
      CANCELLED = "Cancelled", "Cancelled"

   doctor = models.ForeignKey(
      Doctor,
      on_delete=models.CASCADE,
      related_name="appointments",
   )

   patient = models.ForeignKey(
      Patient,
      on_delete=models.CASCADE,
      related_name="appointments",
   )

   appointment_date = models.DateTimeField()

   status = models.CharField(
      max_length=20,
      choices=Status.choices,
      default=Status.PENDING
   )

   def __str__(self):
      return (
         f"{self.patient.name} | "
         f"{self.doctor.name} | "
         f"{self.appointment_date:%d-%m-%Y %I:%M %P}"
      )

   





