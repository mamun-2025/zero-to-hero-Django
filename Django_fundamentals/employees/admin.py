from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "email",
      "department",
      "salary",
      "joining_date",
   )

   list_filter = (
      "department",
      "joining_date",
   )

   search_fields = (
      "name",
      "email",
   )

   ordering = (
      "name",
   )

   list_per_page = 20

   readonly_fields = (
      "created_at",
      "updated_at",
   )

