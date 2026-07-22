from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import AuthorForm, BookForm


# Author List
def author_list(request):

   authors = Author.objects.prefetch_related(
      "books"
   )

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

      


# Book List
def book_list(request):

   books = Book.objects.select_related(
      "author"
   )
   
   return render(
      request,
      "library/book_list.html",
      {
         "books": books,
      },
   )


# Book Detail
def book_detail(request, pk):

   book = get_object_or_404(
      Book,
      pk=pk,
   )

   return render(
      request,
      "library/book_detail.html",
      {
         "book":book,
      },

   )


# Book Create
def book_create(request):
   if request.method == "POST":

      form = BookForm(request.POST)

      if form.is_valid():
         form.save()

         return redirect(
            "library:book_list",
         )
   else:
      form = BookForm()

   return render(
      request,
      "library/book_form.html",
      {
         "form": form,
      },
   )

   

# Book Update
def book_update(request, pk):
   book = get_object_or_404(
      Book,
      pk=pk,
   )

   if request.method == "POST":
      form = BookForm(
         request.POST,
         instance=book,
      )

      if form.is_valid():
         form.save()

         return redirect(
            "library:book_detail",
            pk=book.pk,
         )
   else:
      form = BookForm(
         instance=book,
      )

   return render(
      request,
      "library/book_form.html",
      {
         "form":form,
      },
   )


# Book Delete
def book_delete(request, pk):
   book = get_object_or_404(
      Book,
      pk=pk,
   )

   if request.method == "POST":
      book.delete()

      return redirect(
         "library:book_list",
      )
   
   return render(
      request,
      "library/book_confirm_delete.html",
      {
         "book": book,
      },
   )