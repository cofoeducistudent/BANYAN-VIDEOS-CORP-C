
from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import TemplateView
from shopping_cart.models import ShoppingCartModel

from django.core.mail import send_mail

import os

# Create your views here.


class ContactSent(TemplateView):
    template_name = 'contact_sent/contact_sent.html'

    """
    GET METHOD
    """

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

        SCM = ShoppingCartModel.objects.filter(
            cart_owner=current_user).filter(cart_session=session_key)
        basket_item_count = SCM.count

        context = {

            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,

        }

        return render(request, 'contact_sent/contact_sent.html', context)





    """
    POST METHOD
    """

    def post(self, request):

        SALES_DEPARTMENT_EMAIL = os.getenv("SALES_DEPT")
        BANYAN_VIDEOS_CORP_EMAIL_BOX = os.getenv("BVC_EMAIL_BOX")

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

        message_subject = "** BVC - ENQUIRY ** :" + \
            str(request.POST['subject'])

        message_body = str(request.POST['comment']) + chr(13)+chr(13)


        """
        VALIDATE FORM
        """

        if len(str(request.POST['subject'])) < 4\
        or len(str(request.POST['comment'])) < 4:
            messages.info(
                request, 'Please Include a Proper Subject Field or Message!')
            return redirect('contact')









        """
        SENDMAIL
        
        """

        send_mail(message_subject, message_body, BANYAN_VIDEOS_CORP_EMAIL_BOX,
                  [SALES_DEPARTMENT_EMAIL, request.POST['email']], fail_silently=False)

        messages.info(request, "Message Successfully Sent!")

        context = {

            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,

        }

        return render(request, 'contact_sent/contact_sent.html', context)
