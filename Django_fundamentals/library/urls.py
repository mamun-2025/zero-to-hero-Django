

from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:pk>/", views.author_detail, name="author_detail"),

]
