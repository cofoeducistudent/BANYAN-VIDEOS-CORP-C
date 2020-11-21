from crispy_forms.helper import FormHelper
from home import models
from django import  forms



class LoginForm(forms.Form):
    
    helper = FormHelper
    helper.form_show_labels = False
    
    
    login_form_username = forms.CharField(label='Username')
    login_form_password = forms.CharField(label='Password')
    
    