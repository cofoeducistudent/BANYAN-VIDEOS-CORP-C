from django.http import request
from django.shortcuts import render
from django.views.generic   import TemplateView

# Create your views here.



class Contact(TemplateView):
    template_name = 'contact/contact.html'
    
    
    
    def get(self, request):
        a=1
 

        
        return render (request, 'contact/contact.html' )
 