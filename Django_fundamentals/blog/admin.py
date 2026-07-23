from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

   list_display = (
      "title",
      "content",
   )

   search_fields = (
      "title",
      "content",
   )

   list_filter = (
      "title",
   )

   ordering = (
      "title",
   )

   list_per_page = 10

   readonly_fields = (
      "created_at",
      "updated_at",
   )