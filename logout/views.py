
from django.contrib.auth import logout

from django.shortcuts import render

from django.views.generic import View

from shopping_cart.models import ShoppingCartModel


class Logout(View):

    def get(self, request):

        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key

        current_user = request.user
        if not request.user.is_authenticated:
            current_user = request.user
        if request.user.is_authenticated:
            current_user = request.user

        """
        WIPE OUT CURRENT SEELCTIONS
        """
        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)

        for line_items in SCM:
            line_items.delete()

        """
        LOGOUT USER !
        """
        logout(request)

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        context = {

            'current_user': current_user,

            'SCM': SCM,

            'basket_item_count': basket_item_count,

        }

        return render(request, 'logout/logout.html', context)
