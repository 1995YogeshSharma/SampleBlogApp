from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here

class Home(TemplateView):
    template_name = 'welcome.html'


class Register(generic.CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'registration/register.html'
    success_url = '/home/'
