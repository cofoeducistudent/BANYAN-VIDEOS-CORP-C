from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions


from home import views
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .import models as search_result_models
from .import models as film_models

from django.contrib import messages


# Create your views here.

class SearchResults(TemplateView):
    
    try:
    
        template_name = 'search_results/search_results.html'

        """
        GET GENRE
        """
    
        def get(self, request):
            results_collection = []
       
            all_films = film_models.Films.objects.all()

            sr = request.GET.get('sel_genre')
            for items in all_films:
                if str(items.film_genre) == (sr):
                    results_collection.append(items)

            total_items_found = len(results_collection)
        
            context = {
                'total_items_found': total_items_found,
                'results_collection': results_collection
        
            }
            return render(request, self.template_name, context)

        """
        USE SERACH BOX
        """
        def post(self, request):
            results_collection = []

            all_films = film_models.Films.objects.all()
        
            s_string = request.POST['search_string']
        
            for item in all_films:
                if s_string.upper()  in (item.film_friendly_title).upper():
                    results_collection.append(item)

            total_items_found = len(results_collection)
     
            context = {
            
            'results_collection': results_collection,
            'total_items_found': total_items_found,
               
            }
    
            return render(request, self.template_name, context)

    except Exception as e :
    
        messages.info("An unexpected or illiegal error has occured - redirected to homepage ")
        
        redirect ( views.HomePageView.as_view)