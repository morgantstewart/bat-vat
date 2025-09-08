# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello from BatVat</h1>')

# Define the about view function
def about(request):
    # Send a simple HTML response for the about page
    return HttpResponse('<h1>About BatVat</h1><p>This is the about page for the Bat Vat application!</p>')

# Define the bat index view function
def bat_index(request):
    # Send a simple HTML response for the bats page
    return HttpResponse('<h1>Bats Index</h1><p>Welcome to the bats section!</p>')
