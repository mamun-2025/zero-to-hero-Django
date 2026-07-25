from django.db import models

class Teacher(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   department = models.CharField(max_length=100)

   def __str__(self):
      return self.name 

   class Meta:
      ordering = ["name"]
      verbose_name = "Teacher"
      verbose_name_plural = "Teachers"


class Course(models.Model):
   name = models.CharField(max_length=100)
   code = models.CharField(max_length=20, unique=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   teacher = models.ForeignKey(
      Teacher,
      on_delete=models.CASCADE,
   )

   def __str__(self):
      return self.name 

