from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



def register(request):

   form = RegisterForm(
            request.POST or None
         )

   if request.method == "POST":

      if form.is_valid():

         form.save()

         messages.success(
            request,
            "Your account has been created successfully.",
         )

         return redirect(
            "accounts:login"
         )

   else:

      form = RegisterForm()

   return render(
      request,
      "accounts/register.html",
      {
         "form":form,
      },
   )



def user_login(request):

   form = AuthenticationForm(
      request,
      data=request.POST or None
   )

   if request.method == "POST":

      if form.is_valid():

         username = form.cleaned_data["username"]
         password = form.cleaned_data["password"]

         user = authenticate(
            request,
            username=username,
            password=password,
         )

         messages.success(
            request,
            "Welcome back!",
         )

         if request.POST.get("remember_me"):

            request.session.set_expiray(
               60 * 60 * 24 * 30
            )

         else:
            request.session.set_expiry(0)
         

         if user is not None:

            login(request, user)

            return redirect("accounts:dashboard")

      else:
         messages.error(
            request,
            "Invalid username or password."
         )

   return render(
      request,
      "accounts/login.html",
      {
         "form": form,
      },
   )

# AuthenticationForm নিজেই Valid User Return করতে পারে।

# def user_login(request):

#     form = AuthenticationForm(request, data=request.POST or None)

#     if request.method == "POST":

#         if form.is_valid():

#             login(request, form.get_user())

#             return redirect("home")

#     return render(
#         request, "accounts/login.html", {"form": form}
#     )

# এটি Django-তে বহুল ব্যবহৃত এবং সংক্ষিপ্ত।


def user_logout(request):

   logout(request)

   messages.info(
      request,
      "You have been logged out.",
   )

   return redirect("accounts:login")


@login_required
def dashboard(request):

   return render(
      request,
      "accounts/dashboard.html",
   )


@login_required
def profile(request):

   return render(
      request,
      "accounts/profile.html",
   )


@login_required
def profile_update(request):

   form = ProfileUpdateForm(
      request.POST or None,
      request.FILES or None,
      instance=request.user,
   )

   if request.method == "POST":

      if form.is_valid():

         form.save()

         messages.success(
            request,
            "Profile updated successfully.",
         )

         return redirect("accounts:profile")

   return render(
      request,
      "accounts/profile_update.html",
      {
         "form": form,
      },
   )


def home(request):

   return render(
      request, 
      "accounts/home.html",
   )



@login_required
def change_password(request):

   form = PasswordChangeForm(
      user=request.user,
      data=request.POST or None,
   )

   if request.method == "POST":

      if form.is_valid():

         user = form.save()

         update_session_auth_hash(
            request,
            user,
         )

         messages.success(
            request,
            "Password changed successfylly.",
         )

         return redirect(
            "accounts:profile"
         )


   return render(
      request,
      "accounts/change_password.html",
      {
         "form": form,
      },
   )
