"""_banyanvideos_root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
 
urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', include('home.urls')),
    
    path('search_results/', include('search_results.urls')),
    
    path('login_register/', include('login_register.urls')),
   
    path('logout/', include('logout.urls')),
    
    path('about/', include('about.urls')),
    
    path('shopping_cart/', include('shopping_cart.urls')),
    
    path('members/', include('members.urls')),
    
    path('contact/', include('contact.urls')),
    
    path('my_account/', include('my_account.urls')),
    
    path('delete_from_shopping_cart/', include('delete_from_shopping_cart.urls')),
    
    path('account/', include('allauth.urls')), # added for allauth
    
    path('checkout/', include('checkout.urls')),
    
    path('login_success/', include('login_success.urls')),
    
    path('charge/', include('charge.urls')),
    
]
