# from django.shortcuts import render
# from .forms import EmployeeForm


# def employee_form(request):

#    if request.method == "POST":

#       form = EmployeeForm(request.POST)

#       if form.is_valid():
         
#          print(form.cleaned_data)

#    else:
#       form = EmployeeForm()

#    return render(
#       request,
#       "employees/form.html",
#       {
#          "form":form,
#       },
#    )


from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeModelForm



def employee_list(request):

   employees = Employee.objects.all()

   return render(
      request,
      "employees/employee_list.html",
      {
         "employees": employees,
      },
   )


def employee_detail(request, pk):

   employee = get_object_or_404(
      Employee,
      pk=pk,
   )

   return render(
      request,
      "employees/employee_detail.html",
      {
         "employee": employee,
      },

   )



def employee_create(request):

   if request.method == "POST":

      form = EmployeeModelForm(request.POST)

      if form.is_valid():

         form.save()

         return redirect(
            "employees:employee_list"
         )

   else:
      
      form = EmployeeModelForm()


   return render(
      request,
      "employees/employee_form.html",
      {
         "form":form,
      },
   )



def employee_update(request, pk):
   