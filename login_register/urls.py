
from login_register.views import LoginRegister

from django.urls import path

urlpatterns = [

    path('login_register', LoginRegister.as_view(), name="login_register"),

]
