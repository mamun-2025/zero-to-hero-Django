from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
   list_display = (
      "username",
      "email",
      "phone",
      "is_staff",
      "is_active",
   )

   search_fields = (
      "username",
      "email",
      "phone",
   )

   list_filter = (
      "is_staff",
      "is_active",
   )

   fieldsets = UserAdmin.fieldsets = (
       (
          "Additional Information", 
          {
           "fields": (
               "phone",
               "address",
               "date_of_birth",
           ),
         },
      ),
   )
   
   
