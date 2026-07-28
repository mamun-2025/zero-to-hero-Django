

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):

   class Meta:
      model = User 
      fields = "__all__"

      widgets = {
         "username": forms.TextInput(
            attrs={
               "class": "form-control",
               "placeholder": "Username",
               "required": True,
            }
         ),

         "email": forms.EmailInput(
            attrs={
               "class": "form-control",
               "placeholder": "Email",
               "required": True,
            }
         ),
      }

      def clean_email(self):

         email = self.cleaned_data["email"]

         if User.objects.filter(email=email).exists():

            raise forms.ValidationError(
               "This email is already registered."
            )

         return email


      def clean_phone(self):

         phone = self.cleaned_data("phone")

         if len(phone) != 11:

            raise forms.ValidationError(
               "Phone number must be 11 digits."
            )

         return phone


      # Password Hashing
      def __init__(self, *args, **kwargs):

         super().__init__(*args, **kwargs)

         for field in self.fields.values():

            field.widget.attrs["class"] = "form-control"

         self.fields["password"].widget.attrs["placeholder"] = "Password"

         self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"