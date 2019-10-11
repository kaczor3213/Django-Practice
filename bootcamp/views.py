from django.shortcuts import render, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Client
from .forms import *

def get_sidebar_data():
    user_amount = User.objects.all().count()
    language_amount = ProgrammingLanguage.objects.all().count()
    return {'user_amount': user_amount, 'language_amount': language_amount}

def index(request):
    context = get_sidebar_data()
    return render(request, 'index.html', context=context)

class ClientListView(ListView):
    model = Client
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ClientDetailView(DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'country', 'age', 'language', 'payment']

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'country', 'age', 'language', 'payment']

class ClientDeleteView(DeleteView):
    mode = Client
