
from home import views

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .import models as film_models

from django.contrib import messages

from shopping_cart.models import ShoppingCartModel

# Create your views here.


class SearchResults(TemplateView):

    try:

        template_name = 'search_results/search_results.html'

        """
        GET GENRE
        """

        def get(self, request):

            # CREATE A SESSION IF NOT EXISTING!!
            if not request.session.exists(request.session.session_key):
                request.session.create()
            session_key = request.session.session_key

            current_user = request.user
            if not request.user.is_authenticated:
                current_user = request.user
                
                
            logged_in=False    
            if request.user.is_authenticated:
                logged_in=True
                current_user = request.user

            results_collection = []

            all_films = film_models.Films.objects.all()

            sr = request.GET.get('sel_genre')
            for items in all_films:
                if str(items.film_genre) == (sr):
                    
                    # Add film to results
                    results_collection.append(items)

            total_items_found = len(results_collection)

     

            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

            context = {
                'total_items_found': total_items_found,
                'results_collection': results_collection,

                'basket_item_count': basket_item_count,
                'current_user': current_user,

                'SCM': SCM,
                'logged_in':logged_in,

            }
            return render(request, self.template_name, context)







        """
        USE SERACH BOX
        """

        def post(self, request):

            # CREATE A SESSION IF NOT EXISTING!!
            if not request.session.exists(request.session.session_key):
                request.session.create()
            session_key = request.session.session_key

            current_user = request.user
            if not request.user.is_authenticated:
                current_user = request.user
                
            logged_in=False
            if request.user.is_authenticated:
                logged_in=True
                current_user = request.user

            results_collection = []

            all_films = film_models.Films.objects.all()

            s_string = request.POST['search_string']

            for item in all_films:
                if s_string.upper() in (item.film_friendly_title).upper():
                    #A match for your search was found!!
                    results_collection.append(item)
            total_items_found = len(results_collection)
            
            if int(total_items_found) == 0:
                messages.info(request, 'We could not find any\
                    matches for your search. Please try again!')
                   


            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

            context = {

                'results_collection': results_collection,
                'total_items_found': total_items_found,

                'basket_item_count': basket_item_count,
                'current_user': current_user,

                'SCM': SCM,
                'logged_in':logged_in,
            }

            return render(request, self.template_name, context)

    except Exception as e:

        messages.info(
            "An unexpected or illiegal error has occured - redirected to homepage ")

        redirect(views.HomePageView.as_view)
