from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . models import Person


# Create your views here.
class HomeView(TemplateView):
    template_name = 'myapp/home/home.html'

class AboutView(TemplateView):
    template_name='myapp/home/about.html'

class PeopleView(ListView):
    template_name = 'myapp/home/people.html'
    model = Person
