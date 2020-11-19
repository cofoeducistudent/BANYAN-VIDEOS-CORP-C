from home import models
from django.http import request
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.shortcuts import render
from django.views.generic   import TemplateView


# from shopping_cart import models
from shopping_cart.models  import ShoppingCartModel


# Create your views here.



class Contact(TemplateView):
    template_name = 'contact/contact.html'
    
    
    
    def get(self, request):
    # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create() 
        session_key = request.session.session_key
        
        current_user = request.user
        if not request.user.is_authenticated: 
            current_user = request.user
        if request.user.is_authenticated:
            current_user = request.user
        
        
        
        
        
        
        SCM = ShoppingCartModel.objects.filter(cart_owner=current_user)
        basket_item_count = SCM.count
        
        
        
        
        
        context = {
                    
            'session_key':session_key,
            'current_user':current_user,
            'basket_item_count':basket_item_count,
            
            'SCM': SCM, 
        }
        return render (request, 'contact/contact.html', context )
 