from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Food, Order
from .forms import CategoryForm, FoodForm, OrderForm


# Category
def category_list(request):

   categories = Category.objects.all().order_by("name")

   return render(
      request,
      "restaurant/category_list.html",
      {
         "categories": categories,
      },
   )

    

def category_detail(request, pk):
   category = get_object_or_404(
      Category,
      pk=pk,
   )

   return render(
      request,
      "restaurant/category_detail.html",
      {
         "category": category,
      },
   )



def category_create(request):

   if request.method == "POST":

      form = CategoryForm(
         request.POST
      ) 

      if form.is_valid():

         form.save()

         return redirect(
            "restaurant:category_list"
         )

   else:

      form = CategoryForm()


   return render(
      request,
      "restaurant/category_form.html",
      {
         "form": form,
      },
   )



def category_update(request, pk):

   category = get_object_or_404(
      Category,
      pk=pk,
   ) 

   if request.method == "POST":

      form = CategoryForm(
         request.POST,
         instance=category,
      )

      if form.is_valid():

         form.save()

         return redirect(
            "restaurant:category_list"
         )

   else:

      form = CategoryForm(
         instance=category,
      )

   return render(
      request,
      "restaurant/category_form.html",
      {
         "form": form,
      },
   )



def category_delete(request, pk):

   category = get_object_or_404(
      Category,
      pk=pk,
   )

   if request.method == "POST":

      category.delete()

      return redirect(
         "restaurant:category_list"
      )

   return render(
      request,
      "restaurant/category_confirm_delete.html",
      {
         "category": category,
      },
   )





# Food 
def food_list(request):

   foods =  Food.objects.select_related(
      "category"
   ).order_by(
      "name"
   )

   return render(
      request,
      "restaurant/food_list.html",
      {
         "foods": foods, 
      },
   )



def food_detail(request, pk):

   food = get_object_or_404(

      Food.objects.select_related(
         "category"
      ),
      pk=pk,
   )

   return render(
      request,
      "restaurant/food_detail.html",
      {
         "food": food,
      },
   )


def food_create(request):

   if request.method == "POST":

      form = FoodForm(
         request.POST
      )

      if form.is_valid():

         form.save()

         return redirect(
            "restaurant:food_list"
         )

   else:

      form = FoodForm()

   return render(
      request,
      "restaurant/food_form.html",
      {
         "form": form,
      },
   )



def food_update(request, pk):

   food = get_object_or_404(
      Food,
      pk=pk
   )

   if request.method == "POST":
   
      form = FoodForm(
         request.POST,
         instance=food,
      )
   
      if form.is_valid():
   
         form.save()
   
         return redirect(
            "restaurant:food_list"
         )
   
   else:
   
      form = FoodForm(
         instance=food,
      )
   
   return render(
      request,
      "restaurant/food_form.html",
      {
         "form": form,
      },
   )
   

def food_delete(request, pk):

     food = get_object_or_404(
        Food,
        pk=pk
     )

     if request.method == "POST":
   
         food.delete()
   
         return redirect(
            "restaurant:food_list"
         )
   
     return render(
         request,
         "restaurant/food_confirm_delete.html",
         {
            "food": food,
         },
      )
   



# Order 
def order_list(request):

   orders = Order.objects.prefetch_related(
      "foods"
   ).order_by(
      "-order_date"
   )

   return render(
      request,
      "restaurant/order_list.html",
      {
         "orders": orders,
      },
   )



def order_detail(request, pk):

   order = get_object_or_404(

      Order.objects.prefetch_related(
         "foods"
      ),
      pk=pk,
   )

   return render(
      request,
      "restaurant/order_detail.html",
      {
         "order": order,
      },
   )




def order_create(request):

   if request.method == "POST":

      form = OrderForm(request.POST)

      if form.is_valid():

         form.save()

         return redirect(
            "restaurant:order_list"
         )

   else:

      form = OrderForm()

   return render(
      request,
      "restaurant/order_form.html",
      {
         "form":form,
      },
   )



def order_update(request, pk):

   order = get_object_or_404(
      Order,
      pk=pk
   )

   if request.method == "POST":

      form = OrderForm(
         request.POST,
         instance=order,
      )

      if form.is_valid():

         form.save()

         return redirect(
            "restaurant:order_list"
         )

   else:

      form = OrderForm(
         instance=order,
      )

   return render(
      request,
      "restaurant/order_form.html",
      {
         "form": form,
      },
   )




def order_delete(request, pk):

   order = get_object_or_404(
      Order,
      pk=pk,
   )

   if request.method == "POST":

      order.delete()

      return redirect(
         "restaurant:order_list"
      )

   return render(
      request,
      "restaurant/order_confirm_delete.html",
      {
         "order": order,
      },
   )
