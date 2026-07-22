

from django import forms

class EmployeeForm(forms.Form):

   name = forms.forms.CharField(
      max_length=100
   )

   email = forms.EmailField()

   salary = forms.DecimalField()

   department = forms.CharField(
      max_length=100
   )

   joinin_date = forms.DateField


   