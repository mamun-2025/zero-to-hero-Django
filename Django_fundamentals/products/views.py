
# from django.http import HttpResponse

# def product_list(request):
#    return HttpResponse("Products Page Open.")

# def home(request):
#    return HttpResponse("Home Page Open.")

# def about(request):
#    return HttpResponse("About Page Open.")

# def contact(request):
#    return HttpResponse("Contact Page Open.")



from django.shortcuts import render

def product_list(request):

   context = {
      "title": "My Store",
      "product_name": "Laptop",
      "price": 50000,
      "stock": 20,
      "brand": "HP",
   }

   return render(
      request,
      "products/product_list.html",
      context  
   )