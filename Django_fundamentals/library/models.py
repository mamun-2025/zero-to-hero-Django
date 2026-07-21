from django.db import models


# Author Model
class Author(models.Model):

   name = models.CharField(max_length=100)

   bio = models.TextField(blank=True)

   created_at = models.DateTimeField(auto_now_add=True)

   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.name 
   

# Book Model
class Book(models.Model):

   title = models.CharField(max_length=255)

   price = models.DecimalField(
      max_digits=8, 
      decimal_places=2,
   )

   published_date = models.DateField()

   author = models.ForeignKey(
      Author,
      on_delete=models.CASCADE,

   )

   created_at = models.DateTimeField(auto_now_add=True)

   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.title