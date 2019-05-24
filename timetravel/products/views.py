from django.shortcuts import render

# Create your views here.

def intro(request):
    return render(request, 'products_intro.html')