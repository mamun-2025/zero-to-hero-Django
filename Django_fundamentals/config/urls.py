
from django.contrib import admin
from django.urls import include, path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path("students/", include("students.urls")),
    path("library/", include("library.urls")),
    path("employees/", include("employees.urls")),
    path("blogs/", include("blog.urls")),
]

if settings.DEBUG:
   urlpatterns += static(
      settings.MEDIA_URL,
      document_root=settings.MEDIA_ROOT,
   )







