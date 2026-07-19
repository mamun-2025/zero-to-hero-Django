
from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list),
    # path("home/", views.home),
    # path("about/", views.about),
    # path("contact/", views.contact),
    path("<int:id>/", views.product_detail, name="product_detail"),
    
]
