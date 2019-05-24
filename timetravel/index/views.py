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
        form = LocationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            location = form.cleaned_data['location']

            form=LocationForm

        args = {'form': form, 'location': location}

        return render(request, 'index/home.html', args)







