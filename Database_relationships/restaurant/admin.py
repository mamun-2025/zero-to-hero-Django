from django.contrib import admin
from .models import Category, Food, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "created_at",
   )

   search_fields = (
      "name",
   )

   ordering = (
      "name",
   )

   list_per_page = 20


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "name",
      "category",
      "price",
      "available",
      "created_at",
   )

   list_select_related = (
      "category",
   )

   list_filter = (
      "category",
      "available",
   )

   search_fields = (
      "name",
      "description",
   )

   list_editable = (
      "price",
      "available",
   )

   autocomplete_fields = (
      "category",
   )

   ordering = (
      "category",
      "name",
   )

   list_per_page = 20



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

   list_display = (
      "id",
      "customer_name",
      "status",
      "order_date",
      "food_count",
   )

   list_display_links = (
      "customer_name",
   )

   list_filter = (
      "status",
      "order_date",
   )

   search_fields = (
      "customer_name",
   )

   filter_horizontal = (
      "foods",
   )

   readonly_fields = (
      "order_date",
   )

   ordering = (
      "-order_date",
   )

   date_hierarchy = "order_date"

   list_per_page = 20

   save_on_top = True


   @admin.display(description="Total Foods")
   def food_count(self, obj):
      return obj.foods.count()

