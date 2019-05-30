from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from .forms import LocationForm

# Create your views here.

class HomeView(TemplateView):


    def get(self, request):



        return render(request, 'index/home.html')


    def post(self, request):

        if request.method == 'POST':
            location = request.POST.get('destination')



        return render(request, 'products/products_intro.html', {'location':location})







