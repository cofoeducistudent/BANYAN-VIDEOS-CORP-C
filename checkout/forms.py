from django.forms import Form
from django import forms


class ShippingForm(forms.Form):
    sf_username = forms.CharField(label='Username', max_length=128)

    sf_email = forms.CharField(label='Email', max_length=128)

    sf_address_line1 = forms.CharField(label='Address Line 1', max_length=128)
    sf_address_line2 = forms.CharField(label='Address Line 2', max_length=128)
    sf_address_line3 = forms.CharField(label='Address Line 3', max_length=128)
    sf_post_code = forms.CharField(label='Postcode', max_length=128)
    sf_country = forms.CharField(label='Country', max_length=128)
    sf_transaction_id = forms.CharField(label='Transaction ID',max_length=128)
