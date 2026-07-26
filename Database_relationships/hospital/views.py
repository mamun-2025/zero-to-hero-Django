from django.shortcuts import render
from .models import  Appointment


def appointment_list(request):

   appointments = Appointment.objects.select_related(
      "doctor",
      "patient",
   )

   return render(
      request,
      "hospital/appointment_list.html",
      {
         "appointments": appointments,
      },
   )
