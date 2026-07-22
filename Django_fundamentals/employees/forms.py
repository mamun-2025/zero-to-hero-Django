

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