from django.http import request
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.shortcuts import render
from django.views.generic   import TemplateView



# Create your views here.

class ShoppingCart(TemplateView):
    template_name = 'shopping_cart/shopping_cart.html'


    def get(self,request):
        a=1


        return render (request, 'shopping_cart/shopping_cart.html')