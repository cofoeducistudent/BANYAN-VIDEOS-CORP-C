
from django.shortcuts import render

from django.views.generic import TemplateView
from shopping_cart.models import ShoppingCartModel

from .forms import LoginForm

# Create your views here.


class LoginRegister(TemplateView):
    template_name = "login_register/login_register.html"

    def get(self, request):

        LIF = LoginForm()

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

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        context = {

            'session_key': session_key,
            'current_user': current_user,

            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'LIF': LIF,
            'logged_in':logged_in,
        }

        return render(request, 'login_register/login_register.html', context)
