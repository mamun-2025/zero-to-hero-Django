from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "email",
   )

   search_fields = (
      "name",
      "email",
   )

   ordering = (
      "name",
   )

   readonly_fields = (
      "created_at",
      "updated_at",
   )