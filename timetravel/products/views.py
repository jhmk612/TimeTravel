from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404


# Create your views here.

class intro(TemplateView):


    def get(self, request):


        return render(request, 'products/intro.html')


class gwanghwamun(TemplateView):


    def get(self, request):


        return render(request, 'products/payment.html')

class jamsil(TemplateView):


    def get(self, request):


        return render(request, 'products/index_jamsil.html')


class yeouido(TemplateView):


    def get(self, request):


        return render(request, 'products/index_yeouido.html')