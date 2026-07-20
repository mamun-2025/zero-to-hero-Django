from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):

   students = Student.objects.all()

   return render(
      request,
      "students/student_list.html",
      {
         "students": students,
      },
   )


def student_detail(request, pk):

   student = get_object_or_404(
      Student,
      pk=pk
   )

   return render(
      request,
      "students/student_detail.html",
      {
         "student": student,
      },
   )



def student_create(request):

   if request.method == "POST":

      Student.objects.create(
         name=request.POST["name"],
         email=request.POST["email"],
         age=request.POST["age"],
      )
     
      return redirect(
         "students:student_list"
      )

   return render(
      request,
      "students/student_form.html",
   )



def student_update(request, pk):

   student = get_object_or_404(
      Student,
      pk=pk
   )

   if request.method == "POST":

      student.name = request.POST["name"]
      student.email = request.POST["email"]
      student.age = request.POST["age"]

      student.save()

      return redirect(
         "students:student_list"
      )

   return render(
      request,
      "students/student_update.html",
      {
         "student": student
      }
   )