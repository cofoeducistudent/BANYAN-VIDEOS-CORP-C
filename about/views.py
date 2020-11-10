
from django.urls import path
from django.http import request
from django.shortcuts import render
from django.views.generic   import TemplateView

# Create your views here.



class AboutView(TemplateView):
    template_name = 'about/about.html'
    
    
    def get(self, request):
        
 
        
        
        
        
        
      

        return render (request, 'about/about.html')