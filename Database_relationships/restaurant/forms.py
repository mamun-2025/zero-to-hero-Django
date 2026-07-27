

from django import forms
from .models import Category, Food, Order

class CategoryForm(forms.ModelForm):

   class Meta:
      model = Category
      fields = "__all__"


class FoodForm(forms.ModelForm):

   class Meta:
      model = Food
      fields = "__all__"


class OrderForm(forms.ModelForm):

   class Meta:
      model = Order
      fields = "__all__"

      