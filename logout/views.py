from django.http.response import HttpResponse
from my_account import views
from django.http import request, HttpResponse

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts   import render,redirect
from django.http    import request

from django.views.generic  import View
 
from shopping_cart.models  import ShoppingCartModel
 
 




 
class Logout(View):
    
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
        





        logout(request)

 
 
 
 
 
 
 
 
 
 
 
        
        SCM = ShoppingCartModel.objects.filter(cart_owner = current_user).filter(cart_session = session_key)
        basket_item_count = SCM.count
        
        
        
           
        context = {
            
            'current_user':current_user,
            
            'SCM':SCM, 
             
            'basket_item_count':basket_item_count, 
            
            }
            
        return render( request, 'logout/logout.html', context)