from django.shortcuts import render, redirect

from .forms import LocationForm

# Create your views here.
def home(request):
    return render(request, 'index/home.html')

def locate(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LocationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            location = form.save(commit=False)

            return redirect("index/home.html")

        else:
            form=LocationForm()

        return render(request, 'tour/tour.html', {'form':form})



