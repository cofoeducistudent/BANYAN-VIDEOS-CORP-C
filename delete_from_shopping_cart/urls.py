from django.urls    import path
from .views import DeleteFromShoppingCart



urlpatterns =[
    
    path('delete_from_shopping_cart', DeleteFromShoppingCart.as_view(), name="delete_from_shopping_cart" )
    
    
]