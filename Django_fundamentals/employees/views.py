from django.shortcuts import render
from .forms import EmployeeForm


def employee_form(request):

   if request.method == "POST":

      form = EmployeeForm(request.POST)

      if form.is_valid():
         
         print(form.cleaned_data)

   else:
      form = EmployeeForm()

   return render(
      request,
      "employees/form.html",
      {
         "form":form,
      },
   )


