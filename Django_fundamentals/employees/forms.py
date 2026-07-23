

# # Manual Form
# from django import forms

# class EmployeeForm(forms.Form):

#    name = forms.CharField(
#       max_length=100
#    )

#    email = forms.EmailField()

#    salary = forms.DecimalField()

#    department = forms.CharField(
#       max_length=100
#    )

#    joinin_date = forms.DateField


from django import forms 
from .models import Employee
from django.core.exceptions import ValidationError

class EmployeeModelForm(forms.ModelForm):

   class Meta:
      
      model = Employee

      fields = [
         "name",
         "email",
         "salary",
         "department",
         "joining_date",
      ]

   def clean_email(self):

      email = self.cleaned_data["email"]

      if Employee.objects.filter(email=email).exists():

         raise ValidationError(
            "This email already exists."
         )

      return email



   def clean_salary(self):

      salary = self.cleaned_data["salary"]

      if salary <= 0:
         raise ValidationError(
            "Salary must be greater than zero."
         )

      if salary < 10000:
         raise ValidationError(
            "Minimum salary is 10000"
         )

      return salary