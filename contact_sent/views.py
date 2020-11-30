from django.shortcuts import render
from django.contrib import messages

from django.views.generic import TemplateView
from shopping_cart.models import ShoppingCartModel

from django.core.mail import send_mail

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

        SALES_DEPT_EMAIL = 'cofoedu@gmail.com'

        messages.info(request, "Message Sent!")

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




        message_subject = "BYVC - ENQUIRY : ** " + str(request.POST['subject'])

        message_body = str(request.POST['comment']) + chr(13)+chr(13)

        send_mail(message_subject, message_body, 'cofoedu_banyan@hotmail.com',
                  [SALES_DEPT_EMAIL, request.POST['email']], fail_silently=False)

        context = {

            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,

        }

        return render(request, 'contact_sent/contact_sent.html', context)
