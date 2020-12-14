
from django.shortcuts import render
from django.views.generic import TemplateView

from shopping_cart.models import ShoppingCartModel
from .forms import ContactForm

# Create your views here.


class Contact(TemplateView):
    template_name = 'contact/contact.html'

    """
    GET CODE SECTION
    """

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

        prefill = {}

        """
        IF USER IS REGISTERD - GO GRAB USER NAME 
        AND EMAIL AND PRE-POPULATE TO SAVE TIME
        """
        if request.user.is_authenticated:
            prefill = {
                'username': current_user,
                'email': request.user.email,
            }

        # prefill contact form
        CFM = ContactForm(prefill)

        if CFM.is_valid():
            cd = CFM.cleaned_data
            print(cd)
            CFM = ContactForm(cd)

        context = {

            'session_key': session_key,
            'current_user': current_user,
            'basket_item_count': basket_item_count,

            'SCM': SCM,
            'CFM': CFM,
            'logged_in':logged_in,

        }

        return render(request, 'contact/contact.html', context)
