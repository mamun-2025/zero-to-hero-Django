from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm


# Author List
def author_list(request):

   authors = Author.objects.all()

   return render(
      request,
      "library/author_list.html",
      {
         "authors": authors,
      },
   )


# Author Detail
def author_detail(request, pk):

   author = get_object_or_404(
      Author,
      pk=pk,
   )

   return render(
      request,
      "library/author_detail.html",
      {
         "author":author,
      },
   )


# Author Create
def author_create(request):

   if request.method == "POST":

      form = AuthorForm(request.POST)

      if form.is_valid():
         form.save()

         return redirect(
            "library:author_list"
         )
      
   else:

      form = AuthorForm()

   return render(
      request,
      "library/author_form.html",
      {
         "form": form,
      },
   )



# Author Update
def author_update(request, pk):

   author = get_object_or_404(
      Author,
      pk=pk,
   )

   if request.method == "POST":

      form = AuthorForm(
         request.POST,
         instance=author,
      )

      if form.is_valid():
         form.save()

         return redirect(
            "library:author_detail",
            pk=author.pk,
         )
      
   else:

      form = AuthorForm(
         instance=author,
      )

   return render(
      request,
      "library/author_form.html",
      {
         "form": form,
      },
   )
   


# Author Delete
def author_delete(request, pk):

   author = get_object_or_404(
      Author,
      pk=pk,
   )

   if request.method == "POST":
      
      author.delete()

      return redirect(
         "library:author_list",
      )
   
   return render(
      request,
      "library/author_confirm_delete.html",
      {
         "author": author,
      },
   )

      
