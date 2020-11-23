from django.shortcuts import redirect, render
from django.views.generic   import TemplateView

from shopping_cart.models   import  ShoppingCartModel

from  .forms import ShippingForm


# Create your views here.



class Checkout(TemplateView):
    template_name = 'checkout/checkout.html'
    
    
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
        
        
        SF = ShippingForm()
        
  
  
  
  
  
    
    
        context = {
            
            'basket_item_count': basket_item_count,
            'current_user': current_user,
            
            
            'SCM':SCM,
            'SF':SF,
            
        }
 
        return render(request, self.template_name, context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def post(self, request):
        
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
        
        
        if not basket_item_count:
            return redirect('/')
        
        
        
        
        
        SF = ShippingForm()
 
        TID=session_key
 
        SF.sf_transaction_id = TID
    
    
    
    
    
    
    
        context = {
            'session_key':session_key,
            'basket_item_count': basket_item_count,
            'current_user': current_user,
            
            
            'SCM':SCM,
            'SF':SF,
            
        }
 
        return render(request, self.template_name, context)