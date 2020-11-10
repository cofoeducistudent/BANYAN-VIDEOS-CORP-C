from django.http import request
from django.shortcuts import render

from django.contrib.auth.models  import User


from django.views.generic import TemplateView

# Create your views here.


class LoginRegister(TemplateView):
    template_name="login_register/login_register.html"
    
    
    def login(self, request):
        
        
        
        
        
        
        
        
        return render(request, 'login_register/login_register.html')