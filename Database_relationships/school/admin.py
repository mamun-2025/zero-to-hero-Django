from django.contrib import admin
from .models import Teacher, Course

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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   list_display = (
      "id",
      "name",
      "created_at",
   )

   search_fields = (
      "name",
      "code",
   )

   ordering = (
      "name",
   )

   list_filter = (
      "name",
   )

   list_per_page = 10

   readonly_fields = (
      "created_at",
      "updated_at",
   )

