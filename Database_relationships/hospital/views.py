from django.shortcuts import render, redirect, get_object_or_404
from .models import  Doctor
from .forms import DoctorForm


def doctor_list(request):

   doctors = Doctor.objects.all()

   return render(
      request,
      "hospital/doctor_list.html",
      {
         "doctors": doctors,
      },
   )


def doctor_detail(request, pk):

   doctor = get_object_or_404(
      Doctor,
      pk=pk,
   )

   return render(
      request,
      "hospital/doctor_detail.html",
      {
         "doctor": doctor,
      },
   )



def doctor_create(request):

   if request.method == "POST":

      form = DoctorForm(
         request.POST
      )

      if form.is_valid():

         form.save()

         return redirect(
            "hospital:doctor_list"
         )

   else:
      form = DoctorForm()

   return render(
      request,
      "hospital/doctor_form.html",
      {
         "form": form,
      },
   )



def doctor_update(request, pk):

   doctor = get_object_or_404(
      Doctor,
      pk=pk,
   )

   if request.method == "POST":

      form = DoctorForm(
         request.POST,
         instance=doctor,
      )

      if form.is_valid():

         form.save()

         return redirect(
            "hospital:doctor_list"
         )

   else:

      form = DoctorForm(
         instance=doctor,
      )

   return render(
      request,
      "hospital/doctor_form.html",
      {
         "form": form,
      },
   )


def doctor_delete(request, pk):

   doctor = get_object_or_404(
      Doctor,
      pk=pk,
   )

   if request.method == "POST":

      doctor.delete()

      return redirect(
         "hospital:doctor_list"
      )

   return render(
      request,
      "hospital/doctor_confirm_delete.html",
      {
         "doctor": doctor,
      },
   )


































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
