from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib import sessions
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.forms import widgets
from shopping_cart.models   import  ShoppingCartModel
from shopping_cart  import models


class ContactForm(forms.Form):
 
    username = forms.CharField( label='Username', max_length=254)
    email = forms.EmailField( label='Email', max_length=254)
    subject= forms.CharField(label='Subject', max_length=128)
    comment= forms.CharField(label='Message', widget=forms.Textarea)
     
