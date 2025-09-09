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
    def __init__(self, name, breed, description, age, image):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        self.image = image

# Create a list of Bat instances
bats = [
    Bat('Lolo', 'tabby', 'Kinda rude.', 3, 'css/images/baticon.png'),
    Bat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0, 'css/images/baticon.png'),
    Bat('Fancy', 'bombay', 'Happy fluff ball.', 4, 'css/images/baticon.png'),
    Bat('Bonk', 'selkirk rex', 'Meows loudly.', 6, 'css/images/baticon.png')
]

