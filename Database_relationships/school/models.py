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
      related_name="courses",

   )

   def __str__(self):
      return self.name 


class Student(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField(unique=True)

   courses = models.ManyToManyField(
      Course,
      related_name="students",
   )

   def __str__(self):
      return self.name 


   
      

