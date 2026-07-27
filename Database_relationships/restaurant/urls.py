
from django.urls import path

from . import views

app_name = "restaurant"


urlpatterns = [

   path("category/", views.category_list, name="category_list"),
   path("category/<int:pk>/", views.category_detail, name="category_detail"),
   path("category/create/", views.category_create, name="category_create"),
   path("category/<int:pk>/update/", views.category_update, name="category_update"),
   path("category/<int:pk>/delete/", views.category_delete, name="category_delete"),


   path("food/", views.food_list, name="food_list"),
   path("food/<int:pk>/", views.food_detail, name="food_detail"),
   path("food/create/", views.food_create, name="food_create"),
   path("food/<int:pk>/update/", views.food_update, name="food_update"),
   path("food/<int:pk>/delete/", views.food_delete, name="food_delete"),


   path("order/", views.order_list, name="order_list"),
   path("order/<int:pk>/", views.order_detail, name="order_detail"),
   path("order/create/", views.order_create, name="order_create"),
   path("order/<int:pk>/update/", views.order_update, name="order_update"),
   path("order/<int:pk>/delete/", views.order_delete, name="order_delete"),
    
]
