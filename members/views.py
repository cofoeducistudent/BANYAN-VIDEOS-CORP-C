from django.http import request
from django.shortcuts import render
from django.views.generic   import TemplateView
# Create your views here.



class Members(TemplateView):
    template_name ='members/member.html'
    
    
    def get(self, request):
        
        
        
    
    
    
        return  render(request, 'members/members.html')
    
    
