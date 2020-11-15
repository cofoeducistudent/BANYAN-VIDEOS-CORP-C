from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.http import request
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.shortcuts import render
from django.views.generic   import TemplateView

from .models import ShoppingCartModel


# Create your views here.

class ShoppingCart(TemplateView):
    template_name = 'shopping_cart/shopping_cart.html'


    def post(self, request):
        
        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create() 
        session_key = request.session.session_key
        if not request.user.is_authenticated: 
            current_user = request.user.username
        current_user = request.user.username
        
        
   
        
        
        # GET DATA FROM SELECTED SERACH RESULTS
        qty = request.POST['quantity'] 
      
        
        
        # CONSTRUCT SHOPPING MODEL ENTRY & SAVE
        b = ShoppingCartModel(
        
          
        cart_owner = current_user,
        cart_session = session_key,
        cart_film_quantity = qty,
        cart_film_box_cover_url = request.POST['film_box_cover_url'],
        
        cart_film_sku = request.POST['cart_film_sku'],
        cart_film_title = request.POST['cart_film_title'],
        cart_film_friendly_title = request.POST['cart_film_friendly_title'],
        cart_film_description = request.POST['cart_film_description'],
        cart_film_price = request.POST['cart_film_price'],
        cart_film_product_discount = request.POST['cart_film_product_discount'],
        
          
        )
            
        b.save()
    
        
     
        
        
        
        
        context = {
           
            'session_key':session_key,
            'current_user':current_user,
            
            }

    







        context = {
           
        'session_key':session_key,
        'current_user':current_user,
            
        }

        return render (request, 'shopping_cart/shopping_cart.html', context)