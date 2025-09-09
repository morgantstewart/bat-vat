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
    # Render the bat index template with the bats data
    return render(request, 'bats/index.html', {'bats': bats})

# views.py

class Bat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Cat instances
bats = [
    Bat('Lolo', 'tabby', 'Kinda rude.', 3),
    Bat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Bat('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Bat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

