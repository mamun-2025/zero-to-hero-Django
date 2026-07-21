

from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "created_at",
   )

   search_fields = (
      "name",
      "bio",
   )

   ordering = (
      "name",
   )

   readonly_fields = (
      "created_at",
      "updated_at",
   )



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

   list_display =(
      "id",
      "title",
      "author",
      "price",
      "published_date",
   )

   search_fields =(
      "title",
      "author__name",
   )

   list_filter = (
      "author",
      "published_date",
   )

   ordering = (
      "-created_at",
   )

   list_per_page = 20

   readonly_fields = (
      "created_at",
      "updated_at",
   )
















