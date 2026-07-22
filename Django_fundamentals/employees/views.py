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


from django.shortcuts import render
from .forms import EmployeeModelForm

def employee_create(request):

   if request.method == "POST":

      form = EmployeeModelForm(request.POST)

      if form.is_valid():

         form.save()

   else:
      
      form = EmployeeModelForm()


   return render(
      request,
      "employees/employee_create.html",
      {
         "form":form,
      },
   )