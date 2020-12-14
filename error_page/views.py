from django.shortcuts import render
from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel
from login_success.models import LoginMessages

from django.contrib.auth.models import Group,User

# Create your views here.

class ErrorPage(TemplateView):
    
    template_name = 'error_page/error_page.html'

    def error_page( request):

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

        ALM = LoginMessages.objects.filter(messages_visible=1)

        context = {

            'session_key': session_key,
            'current_user': current_user,

            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'ALM': ALM,
            'logged_in':logged_in,

        }

        return render(request, 'error_page/error_page.html', context)
