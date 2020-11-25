
from _banyanvideos_root.settings import STRIPE_PRIVATE_KEY
from django.shortcuts import render,redirect
from django.views.generic   import TemplateView

from shopping_cart.models   import  ShoppingCartModel

import stripe
 
# Create your views here.




class Charge(TemplateView):
    template_name = 'charge/charge.html'
    
    

    
    
    
    
    
    def post(self, request ):
        
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
        
        """
        EXIT PAYMENT IF NOTHING IN BASKET!
        """
        basket_item_count = 0
        for items in SCM:
            basket_item_count = basket_item_count+1
        if basket_item_count < 1 :
            return redirect('shopping_cart')
        
 
        # WORKOUT BILL FOR CUSTOMER
        total_to_pay = 0
        for line_items in SCM:
            total_to_pay = total_to_pay + line_items.cart_price_paid
        shipping_charge = 0
        if total_to_pay <30:
            shipping_charge = round((total_to_pay * 10 )/100,2)
        final_bill=round((total_to_pay+shipping_charge),2)
        
        final_bill_in_stripe_format=int(final_bill * 100)
 
 
 
 
 
 
        # stripe.api_key = STRIPE_PRIVATE_KEY
 
 
        # def charge(request): # new
        if request.method == 'POST':
                
                stripe.api_key = STRIPE_PRIVATE_KEY    
                
                charge = stripe.Charge.create(
                amount=final_bill_in_stripe_format,
                currency='gbp',
                description='A Banyan-Videos-Corp charge',
                source=request.POST['stripeToken']
                )
     
            # return render(request, 'charge/charge.html')
 
 
 
 
 
  
 
 
        context={
            
            'session_key':session_key,
            'basket_item_count': basket_item_count,
            'current_user': current_user,
            'shipping_charge':shipping_charge,
            'final_bill':final_bill,
            'final_bill_in_stripe_format':final_bill_in_stripe_format,
            
            'SCM':SCM,
            # 'SF':SF,
            
            
        }
 
        return  render (request, 'charge/charge.html', context)