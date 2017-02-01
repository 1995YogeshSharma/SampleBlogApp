
from django.views.generic.base import TemplateView

from django.views import generic

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class Home(TemplateView):
    """
    shows the home page of the site
    """
    template_name = 'welcome.html'


class Register(generic.CreateView):
    """
    allows user to sign up for the website
    """
    form_class = UserCreationForm
    model = User
    template_name = 'registration/register.html'
    success_url = '/home/'
