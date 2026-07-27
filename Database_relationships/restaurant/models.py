from django.db import models


class Category(models.Model):

   name = models.CharField(
      max_length=100, 
      unique=True,
   )

   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name 


class Food(models.Model):

   category = models.ForeignKey(
      Category,
      on_delete=models.CASCADE,
      related_name="foods",
   )

   name = models.CharField(max_length=100)

   price = models.DecimalField(max_digits=8, decimal_places=2)

   description = models.TextField()

   available = models.BooleanField(default=True)

   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name 



class Order(models.Model):

   STATUS_CHOICES = [
      ("Pending", "Pending"),

      ("Preparing", "Preparing"),

      ("Completed", "Completed"),

      ("Cancelled", "Cancelled"),
   ]

   customer_name = models.CharField(max_length=100)

   foods = models.ManyToManyField(
      Food,
      related_name="orders",
   )

   order_date = models.DateTimeField(auto_now_add=True)

   status = models.CharField(
      max_length=20,
      choices=STATUS_CHOICES,
      default="Pending",
   )

   def __str__(self):
      return f"Order: {self.id}"


   
