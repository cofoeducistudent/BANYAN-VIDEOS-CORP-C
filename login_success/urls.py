from django.urls import path
from .views import LoginSuccess

urlpatterns = [

    path('login_success', LoginSuccess.as_view(), name="login_success")

]
