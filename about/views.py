from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.urls import path
from django.http import request
from django.shortcuts import render
from django.views.generic   import TemplateView

# Create your views here.



class AboutView(TemplateView):
    template_name = 'about/about.html'
    
    
    def get(self, request):
        
   # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create() 
        session_key = request.session.session_key
        if not request.user.is_authenticated: 
            current_user = request.user.username
        current_user = request.user.username
        
        
        
        
        
        
        context = {
           
            
            'session_key':session_key,
            'current_user':current_user,
            
            
        }
        
        
        
        
        
      

        return render (request, 'about/about.html', context)