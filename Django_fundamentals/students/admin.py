from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "email",
      "age",
      "created_at",
   )

   search_fields = (
      "name",
      "email",
   )

   list_filter = (
      "age",
      "created_at",
   )

   ordering = (
      "name",
      # "-name",
      # "age",
      # "-age",
   )

   list_per_page = 10
