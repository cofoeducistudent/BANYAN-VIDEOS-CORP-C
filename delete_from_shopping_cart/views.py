from django.contrib import messages

from django.shortcuts import render
from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel

# Create your views here.


class DeleteFromShoppingCart(TemplateView):

    template_name = "delete_from_shopping_cart/delete_from_shopping_cart.html"

    def post(self, request):
        """
        DELETE VIDEO ITEM FROM CART
        dsku = THE pk of the shopping cart item
        """

        if not request.session.exists(request.session.session_key):
            request.session.create()
        session_key = request.session.session_key

        current_user = request.user
        if not request.user.is_authenticated:
            current_user = request.user
        if request.user.is_authenticated:
            current_user = request.user

        message_item = ""
        delete_this = ""

        try:

            delete_this = request.POST['dsku']

            grab_item = ShoppingCartModel.objects.filter(pk=delete_this)
            message_item = grab_item[0].cart_film_friendly_title

            messages.info(request, message_item)

            ShoppingCartModel.objects.filter(pk=delete_this).delete()

            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

        except:

            ShoppingCartModel.objects.filter(pk=delete_this).delete()

            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

        context = {

            'message_item': message_item,

            'current_user': current_user,

            'SCM': SCM,

            'basket_item_count': basket_item_count,

        }

        return render(request, 'delete_from_shopping_cart/delete_from_shopping_cart.html', context)

    def get(self, request):

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

            'current_user': current_user,

            'SCM': SCM,

            'basket_item_count': basket_item_count,

        }

        return render(request, 'delete_from_shopping_cart/delete_from_shopping_cart.html', context)
