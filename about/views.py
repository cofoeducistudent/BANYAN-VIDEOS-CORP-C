
from django.shortcuts import render
from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel

# Create your views here.


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get(self, request):

        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key

        logged_in = False
        current_user = request.user
        if not request.user.is_authenticated:
            current_user = request.user
        if request.user.is_authenticated:
            logged_in = True
            current_user = request.user

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        context = {

            'session_key': session_key,
            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'logged_in': logged_in,
        }

        return render(request, 'about/about.html', context)
