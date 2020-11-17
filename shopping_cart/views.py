from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions
from django.core.checks import messages
from django.db import models
from django.db.models.query import FlatValuesListIterable

from django.http import request
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ShoppingCartModel
from search_results.models import Films as film_models

# Create your views here.

class ShoppingCart(TemplateView):
    template_name = 'shopping_cart/shopping_cart.html'

    def post(self, request):

        unsaved = False

        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key
        if not request.user.is_authenticated:
            current_user = request.user.username
        current_user = request.user.username

        selected_quantity = request.POST['quantity']
        selected_sku = request.POST['sku']
        
        # subtotal = int(selected_qty) * float(request.POST['cart_film_price'])
        # discount = float(request.POST['cart_film_product_discount'])
        # cart_price_paid = subtotal
        # if request.user.is_authenticated:
        #     dp = subtotal - (subtotal * discount/100)
        #     cart_price_paid = round(dp, 2)

        # else:
        #     a = 1
 
        film_wad=[]
        all_films = film_models.objects.all()
        
        for item in all_films:
            if item.film_sku == selected_sku:
                film_wad.append(item)
                
        # ASSEMBLED FILM ITEM
        b = ShoppingCartModel(

        cart_owner = current_user,
        cart_session = session_key,
        cart_film_quantity= selected_quantity,

        cart_price_paid = 0, # calc

        cart_film_genre = film_wad[0].film_genre,
        cart_film_sku = film_wad[0].film_sku,
    
        cart_film_title = film_wad[0].film_title,
        
        cart_film_friendly_title = film_wad[0].film_friendly_title,
    
        cart_film_box_cover_url = film_wad[0].film_box_cover_url,
    
        cart_film_description = film_wad[0].film_description,
    
        cart_film_price = film_wad[0].film_price,
        
        cart_film_product_discount = film_wad[0].film_product_discount,
        
        cart_film_stock_available = film_wad[0].film_stock_available,
        
        cart_film_global_sale = film_wad[0].film_global_sale,
        
        cart_film_clip_link = film_wad[0].film_clip_link,

        )

        b.save()

        SCM = ShoppingCartModel.objects.filter(cart_owner=current_user)

        # DELETE ALL SHOPPING CART WITH SPECIFIC OWNER
        # my_object = ShoppingCartModel.objects.filter(cart_film_quantity = 1)
        # my_object.delete()

        context = {

            'session_key': session_key,
            'current_user': current_user,
            'SCM': SCM,

        }

        return render(request, 'shopping_cart/shopping_cart.html', context)
