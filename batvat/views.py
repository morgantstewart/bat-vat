# main_app/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bat

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
    bats = Bat.objects.all() 
    # Render the bat index template with the bats data
    return render(request, 'bats/index.html', {'bats': bats})



def bat_detail(request, bat_id):
    bat = Bat.objects.get(id=bat_id)
    return render(request, 'bats/detail.html', {'bat': bat})

# main-app/views.py

class BatCreate(CreateView):
    model = Bat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'bats/bat_form.html'
    success_url = '/bats/'

class BatUpdate(UpdateView):
    model = Bat
    fields = ['breed', 'description', 'age']

class BatDelete(DeleteView):
    model = Bat
    success_url = '/bats/'
