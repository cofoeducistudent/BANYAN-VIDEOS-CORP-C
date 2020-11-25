from django.urls    import  path
from .views import Charge

urlpatterns = [
    
    path('checkout', Charge.as_view(), name="charge"),
    
    
]