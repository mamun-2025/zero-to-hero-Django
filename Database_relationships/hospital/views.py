from django.shortcuts import render, redirect, get_object_or_404
from .models import  Doctor, Patient
from .forms import DoctorForm, PatientForm



# Doctor
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




# Patient
def patient_list(request):

   patients = Patient.objects.all()

   return render(
      request,
      "hospital/patient_list.html",
      {
         "patients": patients,
      },
   )




def patient_detail(request, pk):

   patient = get_object_or_404(
      Patient,
      pk=pk,
   )

   return render(
      request,
      "hospital/patient_detail.html",
      {
         "patient": patient,
      },
   )



def patient_create(request):

   if request.method == "POST":

      form = PatientForm(
         request.POST
      )

      if form.is_valid():

         form.save()

         return redirect(
            "hospital:patient_list"
         )

   else:

      form = PatientForm()

   return render(
      request,
      "hospital/patient_form.html",
      {
         "form": form,
      },
   )



def patient_update(request, pk):

   patient = get_object_or_404(
      Patient,
      pk=pk,
   )

   if request.method == "POST":

      form = PatientForm(
         request.POST,
         instance=patient
      )

      if form.is_valid():

         form.save()

         return redirect(
            "hospital:patient_list"
         )

   else:

      form = PatientForm(
         instance=patient,
      )

   return render(
      request,
      "hospital/patient_form.html",
      {
         "form": form,
      },
   )



def patient_delete(request, pk):

   patient = get_object_or_404(
      Patient,
      pk=pk,
   )

   if request.method == "POST":

      patient.delete()

      return redirect(
         "hospital:patient_list"
      )

   return render(
      request,
      "hospital/patient_confirm_delete.html",
      {
         "patient": patient,
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
