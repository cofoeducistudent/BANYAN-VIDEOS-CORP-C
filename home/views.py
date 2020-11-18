from shopping_cart.views import ShoppingCart
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions

from django.contrib import   messages

from home import models
from django import template
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.template.context import ContextDict
from django.views.generic import TemplateView
from .import models as carousel_models
from django.shortcuts  import render

from django.contrib import messages
 

from search_results import models as genre_models
from search_results import models as film_models


from django.contrib  import sessions
from django.contrib.auth.models import User

from shopping_cart.models  import ShoppingCartModel
 
 
 
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/index.html'

 



    def get(self,request):
        carousel = models.FrontPageCarousel.objects.all()
        articles = models.Article.objects.all()
        genre = film_models.Genre.objects.all()
        
        
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
            'carousel':carousel,
            'articles':articles,
            'genre':genre,
            
            'session_key':session_key,
            'current_user':current_user,
            'basket_item_count':basket_item_count,
            
            'SCM': SCM,
            
        }
        return render (request, 'home/index.html', context)
    
    
 


    