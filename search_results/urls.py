from search_results.views import SearchResults
from django.urls import path

urlpatterns = [

    path('search_results', SearchResults.as_view(), name="search_results")

]
