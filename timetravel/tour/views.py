from django.shortcuts import render

from .forms import LocationForm

# Create your views here.
def tour(request):
    return render(request, 'tour.html')



def locate(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LocationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            location = form.save(commit=False)

            return render(request, ('form', form))

        else:
            form=LocationForm()

        return render(request, 'tour.html', {'form':form})