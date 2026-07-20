
from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    # path("home/", views.home),
    # path("about/", views.about),
    # path("contact/", views.contact),
    path("<int:id>/", views.product_detail, name="product_detail"),
    path("create/", views.product_create, name="product_create"),
    path("<int:id>/edit/", views.product_update, name="product_update"),

]
