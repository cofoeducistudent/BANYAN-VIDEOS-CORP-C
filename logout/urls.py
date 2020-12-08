from logout.views import Logout

from django.urls import path

urlpatterns = [

    path('logout', Logout.as_view(), name='logout'),

]
