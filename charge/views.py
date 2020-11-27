from datetime import date, datetime
import re
from django.contrib import messages
from stripe.util import dashboard_link
from _banyanvideos_root.settings import STRIPE_PRIVATE_KEY
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel

from my_account.models import UserPurchaseHistory
import stripe

from django.core.mail import send_mail

# Create your views here.


class Charge(TemplateView):
    template_name = 'charge/charge.html'

    def post(self, request):
        """
        GRAB COMPLETED FORM DETAILS
        FOR CREATING CONF-EMAIL BODY LATER

        """
        
        
        SALES_DEPT_EMAIL = 'cofoedu@gmail.com'
        
        
        
        
        customer_details = chr(13)
        
        customer_details = customer_details + "<< BANYAN-VIDEOS-CORP. ORDER RECEIPT >>"+chr(13)
        customer_details = customer_details + "TRANSACTION_ID" + \
            request.POST['sf_transaction_id']+chr(13)
        customer_details = customer_details + \
            "----------------------------"+chr(13)
        customer_details = customer_details + \
            request.POST['sf_username']+chr(13)
        customer_details = customer_details + request.POST['sf_email']+chr(13)
        customer_details = customer_details + \
            "----------------------------"+chr(13)
        customer_details = customer_details + \
            request.POST['sf_address_line1']+chr(13)
        customer_details = customer_details + \
            request.POST['sf_address_line2']+chr(13)
        customer_details = customer_details + \
            request.POST['sf_address_line3']+chr(13)
        customer_details = customer_details + \
            request.POST['sf_post_code']+chr(13)
        customer_details = customer_details + \
            request.POST['sf_country']+chr(13)
        customer_details = customer_details + \
            "----------------------------"+chr(13)

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

        """
        EXIT PAYMENT IF NOTHING IN BASKET!
        """
        basket_item_count = 0
        for items in SCM:
            basket_item_count = basket_item_count+1
        if basket_item_count < 1:
            return redirect('shopping_cart')







        # WORKOUT BILL FOR CUSTOMER
        total_to_pay = 0
        for line_items in SCM:
            total_to_pay = total_to_pay + line_items.cart_price_paid
        shipping_charge = 0
        if total_to_pay < 30:
            shipping_charge = round((total_to_pay * 10)/100, 2)
        final_bill = round((total_to_pay+shipping_charge), 2)

        final_bill_in_stripe_format = int(final_bill * 100)

    

        """
        GO AND MAKE A CHARGE TO STRIPE USING RECEIVED TOKEN !!!
        """
        try:

            if request.method == 'POST':

                stripe.api_key = STRIPE_PRIVATE_KEY

                charge = stripe.Charge.create(
                    amount=final_bill_in_stripe_format,
                    currency='gbp',
                    description='A Banyan-Videos-Corp charge',
                    source=request.POST['stripeToken']
                )

            """
            SEND OUT EMAIL RECEIPT
            """
            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

            message_body = ""
            message_body = message_body + customer_details+chr(13)

            for items in SCM:
                p1 = items.cart_film_quantity
                p2 = items.cart_film_friendly_title
                p3 = items.cart_film_sku

                squashed = str(p1)+" x " + str(p2)+" : "+str(p3)

                message_body = message_body + squashed + chr(13)

            message_body = message_body + "£ " + \
                str(final_bill)+chr(13) + chr(13)

            send_mail('BANYAN-VIDEOS-SALES ORDER!', message_body,
                      'cofoedu_banyan@hotmail.com', [ SALES_DEPT_EMAIL,  request.POST['sf_email']], fail_silently=False)


            """
            SALE COMPLETE ......THIS USER IS ANONYMOUS, THEREFORE DELETE ITEMS IN CART!!
            """
            if not request.user.is_authenticated:
                for items in SCM:
                    SCM.filter(cart_owner=current_user).filter(
                        cart_session=session_key).delete()



        except Exception as e:
            messages.info(
                request, 'This Transcation request Failed! Please ensure you are not repeating the Transaction! / ' + str(e))
            
            redirect('home')











        else:

            """
            ///////////////////////////////// LOGGED IN USER PROCESSING /////////
            """
        
            
        if request.user.is_authenticated:
            """
            IF A LOGGED IN USER
            SAVE .....CONTENTS OF CART TO PURCHASE HISTORY!!
            """
            messages.info(request,'WANNABE!!')
 
            dtd = str(date.today())
           

            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

            for items in SCM:

                TID = str(current_user)+":"+str(session_key)

                b = UserPurchaseHistory(

                    ph_purchase_date=dtd,
                    ph_cart_owner=current_user,
                    ph_transaction_id=TID,
                    ph_cart_film_quantity=items.cart_film_quantity,
                    ph_cart_price_paid=items.cart_price_paid,
                    ph_cart_film_genre=items.cart_film_genre,
                    ph_cart_film_sku=items.cart_film_sku,
                    ph_cart_film_title=items.cart_film_title,
                    ph_cart_film_friendly_title=items.cart_film_friendly_title,
                    ph_cart_film_box_cover_url=items.cart_film_box_cover_url,
                    ph_cart_film_description=items.cart_film_description,
                    ph_cart_film_price=items.cart_film_price,
                    ph_cart_film_product_discount=items.cart_film_product_discount,

                )

                b.save()

            """
            SEND OUT CONFIRMATION EMAIL TO SALES
            """
            SCM = ShoppingCartModel.objects.filter(
                cart_owner=current_user).filter(cart_session=session_key)
            basket_item_count = SCM.count

            message_body = ""
            message_body = message_body + customer_details + chr(13)

            for items in SCM:
                p1 = items.cart_film_quantity
                p2 = items.cart_film_friendly_title
                p3 = items.cart_film_sku

                squashed = str(p1)+" x " + str(p2)+" : "+str(p3)

                message_body = message_body + squashed + chr(13)

            message_body = message_body + "£ " + \
                str(final_bill)+chr(13)+chr(13)

            send_mail('BANYAN-VIDEOS-SALES ORDER!', message_body,
                      'cofoedu_banyan@hotmail.com', [ SALES_DEPT_EMAIL, request.POST['sf_email']], fail_silently=False)

            """
            DELETE ITEMS IN CART!!
            """
            for items in SCM:
                SCM.filter(cart_owner=current_user).filter(
                    cart_session=session_key).delete()



        context = {

            'session_key': session_key,
            'basket_item_count': basket_item_count,
            'current_user': current_user,
            'shipping_charge': shipping_charge,
            'final_bill': final_bill,
            'final_bill_in_stripe_format': final_bill_in_stripe_format,

            'SCM': SCM,

        }

        return render(request, 'charge/charge.html', context)
