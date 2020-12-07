from _banyanvideos_root.settings import MAINTENANCE

from home import models

from django.views.generic import TemplateView

from django.shortcuts import render

from search_results import models as film_models

from shopping_cart.models import ShoppingCartModel

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):

        MA = MAINTENANCE
        print(MA)

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

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        context = {
            'carousel': carousel,
            'articles': articles,
            'genre': genre,

            'session_key': session_key,
            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'MA': MA,

        }
        return render(request, 'home/index.html', context)
