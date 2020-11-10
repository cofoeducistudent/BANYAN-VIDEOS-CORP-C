from django.http import request
from django.shortcuts import render
from django.views.generic   import  TemplateView

# Create your views here.


class Logout(TemplateView):
    template_name = 'logout/logout.html'
    
    
    def get(self, request):
        a=1
        
        
        
        return render(request, 'logout/logout.html')
