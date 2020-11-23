from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib import sessions
from django.contrib.auth import authenticate, login, logout, get_user_model

class UserProfileForm(forms.Form):
 
    username = forms.CharField( max_length=254)
    first_name = forms.CharField( max_length=254)
    last_name = forms.CharField( max_length=254 )

    email = forms.EmailField( max_length=254)
    address_line1 = forms.CharField( max_length=254)
    address_line2 = forms.CharField( max_length=254)
    address_line3 = forms.CharField( max_length=254)
    post_code = forms.CharField( max_length=254)
    country = forms.CharField( max_length=254)

   