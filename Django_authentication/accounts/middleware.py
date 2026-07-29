

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone
from django.conf import settings


class AutoLogoutMiddleware:

   def __init__(self, get_response):

      self.get_response = get_response

   def __call__(self, request):

      if request.user.is_authenticated:

         last_activity = request.session.get(
            "last_activity"
         )

         current_time = timezone.now().timestamp()

         timeout = settings.AUTO_LOGOUT_DELAY 

         if last_activity:

            if current_time - last_activity > timeout:

               logout(request)

               return redirect(
                  "accounts:login"
               )

         request.session[
            "last_activity"
         ] = current_time

      response = self.get_response(request)

      return response
      