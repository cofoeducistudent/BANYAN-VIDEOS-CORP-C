
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel

from search_results.models import Films
from home.models import Snippet

# Create your views here.


class Members(TemplateView):
    template_name = 'members/member.html'

    def get(self, request):

        FLM = Films.objects.all()
        SNP = Snippet.objects.all()

    # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key

        current_user = request.user
        if not request.user.is_authenticated:

            return redirect("login_register")

        logged_in=False
        if request.user.is_authenticated:
            logged_in=True
            current_user = request.user

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        context = {

            'session_key': session_key,
            'current_user': current_user,
            'basket_item_count': basket_item_count,
            'SCM': SCM,
            'FLM': FLM,
            'SNP': SNP,
            'logged_in':logged_in,
        }

        return render(request, 'members/members.html', context)
