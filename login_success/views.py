from django.shortcuts import render
from django.views.generic   import  TemplateView




# Create your views here.



class LoginSuccess(TemplateView):
    template_name = 'login_success/login_success.html'
    
    
    def get(self, request):
        
        a=1  
        
        
        
        
        
        
        
        
        
        
        
        
        
        return  render (request, 'login_success/login_success.html' )