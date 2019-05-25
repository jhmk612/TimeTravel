from django.views.generic import TemplateView
from django.shortcuts import render

from .forms import LocationForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index/home.html'

    def get(self, request):
        form = LocationForm()


        return render(request, self.template_name, {'form': form})


    def post(self, request):
        if request.method == 'POST':
            location = request.POST.get('location')



        return render(request, 'index/home.html', {'location':location})







