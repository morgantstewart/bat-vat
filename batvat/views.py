# main_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bat
from .forms import FeedingForm


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
    feeding_form = FeedingForm()
    return render(request, 'bats/detail.html', {
        'bat': bat, 'feeding_form': feeding_form
    })

class BatCreate(CreateView):
    model = Bat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'bats/bat_form.html'
    success_url = '/bats/'

class BatUpdate(UpdateView):
    model = Bat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'bats/bat_form.html'
    success_url = '/bats/'

class BatDelete(DeleteView):
    model = Bat
    template_name = 'bats/bat_confirm_delete.html'
    success_url = '/bats/'

def add_feeding(request, bat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():

        new_feeding = form.save(commit=False)
        new_feeding.bat_id = bat_id
        new_feeding.save()
    return redirect('bat-detail', bat_id=bat_id)

