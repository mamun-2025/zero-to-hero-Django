

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



#### Most Important 
# from django import forms 
# from .models import Employee
# from django.core.exceptions import ValidationError

# class EmployeeModelForm(forms.ModelForm):

#    class Meta:
      
#       model = Employee

#       fields = [
#          "name",
#          "email",
#          "salary",
#          "department",
#          "joining_date",
#       ]

#       widgets = {

#          "name": forms.TextInput(
#             attrs={
#                "class": "form-control",
#                "placeholder": "Enter employee name",
#                "required": True,
#             }
#          ),

#          "email": forms.EmailInput(
#             attrs={
#                "class": "form-control",
#                "placeholder": "Enter email",
#                "required": True,
#             }
#          ),

#          "salary": forms.NumberInput(
#             attrs={
#                "class": "form-control",
#                "placeholder": "Enter salary",
#                "min": 0,
#                "step": "0.01",
#             }
#          ),

#          "department": forms.TextInput(
#             attrs={
#                "class": "form-control",
#                "placeholder": "Enter Department",
#             }
#          ),

#          "joining_date": forms.DateInput(
#             attrs={
#                "class": "form-control",
#                "type": "date",
#             }
#          ),
#       }



#    def clean_email(self):

#       email = self.cleaned_data["email"]

#       if Employee.objects.filter(email=email).exists():

#          raise ValidationError(
#             "This email already exists."
#          )

#       return email



#    def clean_salary(self):

#       salary = self.cleaned_data["salary"]

#       if salary <= 0:
#          raise ValidationError(
#             "Salary must be greater than zero."
#          )

#       if salary < 10000:
#          raise ValidationError(
#             "Minimum salary is 10000"
#          )

#       return salary



from django import forms
from .models import Employee
from django.core.exceptions import ValidationError
from datetime import date 

class EmployeeModelForm(forms.ModelForm):
    
   class Meta:
        
      model = Employee
      fields = "__all__"


      widgets = {

         "name": forms.TextInput(
            attrs={
               "class": "form-control",
               "placeholder": "Enter employee name",
               "required": True,
            }
         ),

         "email": forms.EmailInput(
            attrs={
               "class": "form-control",
               "placeholder": "Enter email",
               "required": True,
            }
         ),

         "department": forms.TextInput(
            attrs={
               "class": "form-control",
               "placeholder": "Enter department",
            }
         ),

         "salary": forms.NumberInput(
            attrs={
               "class": "form-control",
               "placeholder": "Enter salary",
               "min": 0,
               "step": "0.01",
            }
         ),

         "joining_date": forms.DateInput(
            attrs={
               "class": "form-control",
               "type": "date",
            }
         ),
      }



   # Multiple Field Validation
   def clean(self):

      cleaned_data = super().clean()

      department = cleaned_data.get("department")

      salary = cleaned_data.get("salary")

      joining_date = cleaned_data.get("joining_date")

      if (department == "HR" and salary < 20000):

         self.add_error(
            "salary",
            "HR salary must be at least 20000."
         )

      if (department == "IT" and salary < 30000):

         raise ValidationError(
            "IT salary must be at least 30000."
         )

      if (department == "Finance" and joining_date > date.today()):

         raise ValidationError(
            "Joinig date cannot be in the future."
         )

      return cleaned_data

   


