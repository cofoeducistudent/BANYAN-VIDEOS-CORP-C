from django.urls import path
from .views import MyAccount

urlpatterns = [

    path('my_account', MyAccount.as_view(), name="my_account")

]
