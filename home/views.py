
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

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home/index.html'




    def get(self,request):
        carousel = models.FrontPageCarousel.objects.all()
        articles = models.Article.objects.all()
        genre = film_models.Genre.objects.all()
        
        
        context = {
            'carousel':carousel,
            'articles':articles,
            'genre':genre
        }
        return render (request, 'home/index.html', context)
    
    
 


    