from django.http.response import HttpResponse
from my_account import views
from django.http import request, HttpResponse

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts   import render,redirect
from django.http    import request

from django.views.generic  import View
 
 
 
 




 
class Logout(View):
    def get(self, request):

        logout(request)

        
 
        return render( request, 'logout/logout.html')