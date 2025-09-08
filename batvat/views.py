# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Render the home template
    return render(request, 'home.html')

# Define the about view function
def about(request):
    # Render the about template
    return render(request, 'bats/about.html')

# Define the bat index view function
def bat_index(request):
    # Render the bat index template
    return render(request, 'bats/index.html')
