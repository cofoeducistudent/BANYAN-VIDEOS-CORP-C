from django.urls import path

from .views import ShoppingCart

urlpatterns = [

    path('shopping_cart', ShoppingCart.as_view(), name="shopping_cart")

]
