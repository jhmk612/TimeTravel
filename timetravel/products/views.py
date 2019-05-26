from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class intro(TemplateView):


    def get(self, request):


        return render(request, 'products/intro.html')


