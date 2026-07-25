from django.contrib import admin
from .models import Teacher, Course, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "email",
      'department',
   )

   search_fields = (
      "name",
      "email",
   )

   list_filter = (
      "department",
   )

   ordering = (
      "name",
   )

   list_per_page = 20


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   list_display = (
      "id",
      "name",
      "code",
      "teacher"
   )

   search_fields = (
      "name",
      "code",
   )

   ordering = (
      "name",
   )

   list_filter = (
      "teacher",
   )

   list_per_page = 20

   readonly_fields = (
      "created_at",
      "updated_at",
   )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   list_display = (
      "id",
      "name",
      "email",
   )

   list_filter = (
      "name",
   )

   search_fields = (
      "name",
      "email",
   )

   filter_horizontal = (
      "courses",
   )

  