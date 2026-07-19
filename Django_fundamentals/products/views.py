
# from django.http import HttpResponse

# def product_list(request):
#    return HttpResponse("Products Page Open.")

# def home(request):
#    return HttpResponse("Home Page Open.")

# def about(request):
#    return HttpResponse("About Page Open.")

# def contact(request):
#    return HttpResponse("Contact Page Open.")



# from django.shortcuts import render

# def product_list(request):

#    context = {
#       "title": "My Store",
#       "product_name": "Laptop",
#       "price": 50000,
#       "stock": 20,
#       "brand": "HP",
#    }

#    return render(
#       request,
#       "products/product_list.html",
#       context  
#    )



# from django.shortcuts import render
# from .models import Product

# def product_list(request):

#    products = Product.objects.all()

#    context = {
#       "products": products,
#    }

#    return render(
#       request,
#       "products/product_list.html",
#       context,
#    )



# from django.shortcuts import render
# from  .models import Product

# def product_list(request):

#    products = Product.objects.all()

#    return render(
#       request,
#       "products/product_list.html",
#       {
#          "products": products,
#       },
#    )




from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):

   products = Product.objects.all()

   return render(
      request,
      "products/product_list.html",
      {
         "products": products,
      },
   )


def product_detail(request, id):

   product = get_object_or_404(
      Product,
      id=id
   )

   return render(
      request,
      "products/product_detail.html",
      {
         "product": product,
      },
   )



def product_create(request):

   if request.method == "POST":

      name = request.POST["name"]

      price = request.POST["price"]

      stock = request.POST["stock"]

      Product.objects.create(
         name=name,
         price=price,
         stock=stock,
      )

      return redirect(
         "products:product_list"
      )

   return render(
      request,

      "products/product_create.html",
      
   )