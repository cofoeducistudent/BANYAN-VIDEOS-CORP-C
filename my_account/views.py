from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions


from django.shortcuts import render,redirect
from django.views.generic   import TemplateView


# Create your views here.


class MyAccount(TemplateView):
    template_name = 'my_account/my_account.html'
    
    
    def get(self, request):
        a=1
     
     
        return render(request,'my_account/my_account.html' )   
    
    
    
    
    
    
   
