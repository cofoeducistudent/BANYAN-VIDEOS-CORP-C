from datetime import date

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ShoppingCartModel
from search_results.models import Films as film_models

from _banyanvideos_root.settings import FREE_SHIPPING_THRESHOLD

# Create your views here.


class ShoppingCart(TemplateView):
    template_name = 'shopping_cart/shopping_cart.html'

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

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)

        basket_item_count = SCM.count

        # WORKOUT BILL FOR CUSTOMER
        total_to_pay = 0
        for line_items in SCM:
            total_to_pay = total_to_pay + line_items.cart_price_paid
        shipping_charge = 0
        if total_to_pay < float(FREE_SHIPPING_THRESHOLD):
            shipping_charge = round((total_to_pay * 10)/100, 2)
        final_bill = round((total_to_pay+shipping_charge), 2)

        context = {

            'session_key': session_key,
            'current_user': current_user,

            'basket_item_count': basket_item_count,
            'total_to_pay': total_to_pay,
            'shipping_charge': shipping_charge,
            'final_bill': final_bill,

            'SCM': SCM,
            'FREE_SHIPPING_THRESHOLD': str(FREE_SHIPPING_THRESHOLD),
            'logged_in':logged_in,
        }

        return render(request, 'shopping_cart/shopping_cart.html', context)

    def post(self, request):

        unsaved = False

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
        
        

        selected_quantity = int(request.POST['quantity'])
        selected_sku = request.POST['sku']

        price_paid = 0
        film_wad = []
        all_films = film_models.objects.all()

        for item in all_films:
            if item.film_sku == selected_sku:
                film_wad.append(item)

                """
                Work out charge on server side for security
                """

                item_price = film_wad[0].film_price
                item_discount = film_wad[0].film_product_discount
                price_paid = (film_wad[0].film_price * selected_quantity)

                if request.user.is_authenticated:
                    price_paid_member = (
                        item_price) - (((item_price * item_discount)/100) * selected_quantity)
                    price_paid = (price_paid_member * selected_quantity)

                price_paid = round(price_paid, 2)

        tdate = str(date)

        # ASSEMBLED FILM ITEM
        b = ShoppingCartModel(

            cart_owner=request.user,
            cart_session=session_key,

            cart_film_quantity=selected_quantity,

            cart_price_paid=price_paid,

            cart_film_genre=film_wad[0].film_genre,
            cart_film_sku=film_wad[0].film_sku,

            cart_film_title=film_wad[0].film_title,

            cart_film_friendly_title=film_wad[0].film_friendly_title,

            cart_film_box_cover_url=film_wad[0].film_box_cover_url,

            cart_film_description=film_wad[0].film_description,

            cart_film_price=film_wad[0].film_price,

            cart_film_product_discount=film_wad[0].film_product_discount,

            cart_film_stock_available=film_wad[0].film_stock_available,

            cart_film_global_sale=film_wad[0].film_global_sale,

            cart_film_clip_link=film_wad[0].film_clip_link,

        )

        b.save()

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)

        basket_item_count = SCM.count

        # WORKOUT BILL FOR CUSTOMER
        total_to_pay = 0
        for line_items in SCM:
            total_to_pay = total_to_pay + line_items.cart_price_paid
        shipping_charge = 0
        if total_to_pay < float(FREE_SHIPPING_THRESHOLD):
            shipping_charge = round((total_to_pay * 10)/100, 2)
        final_bill = round((total_to_pay+shipping_charge), 2)

        context = {

            'session_key': session_key,
            'current_user': current_user,

            'basket_item_count': basket_item_count,
            'total_to_pay': total_to_pay,
            'shipping_charge': shipping_charge,
            'final_bill': final_bill,

            'SCM': SCM,
            'FREE_SHIPPING_THRESHOLD': str(FREE_SHIPPING_THRESHOLD),
            'logged_in':logged_in,
        }

        return render(request, 'shopping_cart/shopping_cart.html', context)
