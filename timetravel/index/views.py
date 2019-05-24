from django.shortcuts import render, redirect

from .forms import LocationForm

# Create your views here.
def home(request):
    return render(request, 'index/home.html')

'''def get(request):
    if request.method == 'GET':
        form=LocationForm(request.GET)
        return redirect(request, 'index/home.html', {'form': form})'''


def locate(request):

    if request.method == 'POST': # If the form has been submitted...
        form = LocationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            location = form.cleaned_data.get['location']

        args = {'form': form, 'location': location}

        return render(request, 'index/home.html', args)







