
from django.http import HttpResponse

def product_list(request):
   return HttpResponse("Products Page Open.")

def home(request):
   return HttpResponse("Home Page Open.")

def about(request):
   return HttpResponse("About Page Open.")

def contact(request):
   return HttpResponse("Contact Page Open.")



