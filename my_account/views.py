 
from django.db import models
from my_account.models import UserProfile
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import sessions
from django.db.models.fields import NullBooleanField
from django.contrib import messages

from django.shortcuts import render,redirect
from django.views.generic   import TemplateView

from shopping_cart.models  import ShoppingCartModel

from .forms import  UserProfileForm



from . import models as UPAD

# Create your views here.










class MyAccount(TemplateView):
    template_name = 'my_account/my_account.html'
    
    """
    GET
    """
    def get(self, request):
        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create() 
        session_key = request.session.session_key
        
        current_user = request.user
        if not request.user.is_authenticated: 
            return redirect("login_register")
        if request.user.is_authenticated:
            current_user = request.user
        

        SCM = ShoppingCartModel.objects.filter(cart_owner = current_user).filter(cart_session = session_key)
        basket_item_count = SCM.count

        UPD = UserProfile.objects.filter(up_username=current_user)

        
    
    
        c = UserProfile.objects.all().filter(up_username = str(current_user) )
        
        """
        LOAD UP USER PROFILE FORM
        """
        preload = {
            
            'username':current_user,
            'email': request.user.email,
            
            'first_name':UPD[0].up_first_name,
            'last_name':UPD[0].up_last_name,
            'address_line1':UPD[0].up_address_line1,
            'address_line2':UPD[0].up_address_line2,
            'address_line3':UPD[0].up_address_line3,
            'post_code':UPD[0].up_post_code,
            'country':UPD[0].up_country,
            
            
            }
        
        UPF = UserProfileForm(preload)

 










        context = {
           
        'session_key':session_key,
        'current_user':current_user,
        'basket_item_count':basket_item_count,
        
        'SCM':SCM,
        'UPF':UPF,
        
        }
     
        return render(request,'my_account/my_account.html', context )   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    POST
    """
    def post(self, request):
        # CREATE A SESSION IF NOT EXISTING!!
        if not request.session.exists(request.session.session_key):
            request.session.create() 
        session_key = request.session.session_key
        
        current_user = request.user
        if not request.user.is_authenticated: 
            return redirect("login_register")
        if request.user.is_authenticated:
            current_user = request.user
 
        SCM = ShoppingCartModel.objects.filter(cart_owner = current_user).filter(cart_session = session_key)
        basket_item_count = SCM.count






        # UPROFILEDATA = UserProfile.objects.all()

        """
        SAVE PROFILE
        """
        
        c = UserProfile.objects.all().filter(up_username = str(current_user) )
        c.delete()
        
        b = UPAD.UserProfile (
 
            up_username = current_user,
            up_first_name = (request.POST['first_name']),
            up_last_name = (request.POST['last_name']),

            # up_email = (request.POST['email']), 
            up_email = request.user.email,
            up_address_line1 = (request.POST['address_line1']),
            up_address_line2 =(request.POST['address_line2']),
            up_address_line3 =(request.POST['address_line3']),
            up_post_code = (request.POST['post_code']),
            up_country = (request.POST['country']),
            
        )
 
        b.save()
        
        messages.info(request,"Your Profile has been Saved")
        
        return redirect ('home')
        
        
        
        
        
        preload = {
            
            'username':current_user,
            'email': request.user.email,
    
        }
        
        UPF = UserProfileForm(preload)

 

        context = {
           
        'session_key':session_key,
        'current_user':current_user,
        'basket_item_count':basket_item_count,
        
        'SCM':SCM,
        'UPF':UPF,
        
        }
     
        return render(request,'my_account/my_account.html', context )  
    
    
   
