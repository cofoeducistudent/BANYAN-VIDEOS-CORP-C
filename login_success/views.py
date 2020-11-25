from django.shortcuts import render
from django.views.generic   import  TemplateView

from shopping_cart.models   import  ShoppingCartModel
from login_success.models   import  LoginMessages

# Create your views here.



class LoginSuccess(TemplateView):
    template_name = 'login_success/login_success.html'
    
    
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
        
        
        
        SCM = ShoppingCartModel.objects.filter(cart_owner = current_user).filter(cart_session = session_key)

        basket_item_count = SCM.count
        
        ALM = LoginMessages.objects.filter(messages_visible= 1 )
        
        
        
        
        
        
        
        
        context = {

            'session_key': session_key,
            'current_user': current_user,
            
            'basket_item_count':basket_item_count,
 
            'SCM': SCM,
            'ALM':ALM,
            
        }

        return  render (request, 'login_success/login_success.html', context )