# main_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bat, Toy
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Import HttpResponse to send text-based responses
from django.http import HttpResponse

class Home(LoginView):
    template_name = 'home.html'


# Define the about view function
def about(request):
    # Render the about template
    return render(request, 'bats/about.html')

@login_required
def bat_index(request):
    bats = Bat.objects.filter(user=request.user)
    return render(request, 'bats/index.html', {'bats': bats})



def bat_detail(request, bat_id):
    bat = Bat.objects.get(id=bat_id)
    feeding_form = FeedingForm()
    return render(request, 'bats/detail.html', {
        'bat': bat, 'feeding_form': feeding_form
    })

class BatCreate(LoginRequiredMixin, CreateView):
    model = Bat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'bats/bat_form.html'
    success_url = '/bats/'
    
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the bat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bat-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class BatUpdate(LoginRequiredMixin, UpdateView):
    model = Bat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'bats/bat_form.html'
    success_url = '/bats/'

class BatDelete(LoginRequiredMixin, DeleteView):
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

# Toy Views
@login_required
def toy_index(request):
    toys = Toy.objects.filter(user=request.user)
    return render(request, 'toys/index.html', {'toys': toys})

def toy_detail(LoginRequiredMixin,request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys/detail.html', {'toy': toy})

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = ['name', 'color']
    template_name = 'toys/toy_form.html'
    success_url = '/toys/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']
    template_name = 'toys/toy_form.html'
    success_url = '/toys/'

class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    template_name = 'toys/toy_confirm_delete.html'
    success_url = '/toys/'