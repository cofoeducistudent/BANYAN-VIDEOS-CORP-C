from django.http import request
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions


from django.shortcuts import render
from django.views.generic   import TemplateView
# Create your views here.



class Members(TemplateView):
    template_name ='members/member.html'
    
    
    def get(self, request):
        
        
        
    
    
    
        return  render(request, 'members/members.html')
    
    
