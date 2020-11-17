from django.shortcuts import render
from django.views.generic   import TemplateView

# Create your views here.


class DeleteFromShoppingCart(TemplateView):
    template_name= "delete_from_shopping_cart/delete_from_shopping_cart.html"
    
    
    def get (self, request):
        a=1
        
        
        
        
        
        
        
        return render(request, 'delete_from_shopping_cart/delete_from_shopping_cart.html' )
    