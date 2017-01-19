from django.shortcuts import render
from django.views.generic import CreateView
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AddBlog(LoginRequiredMixin, CreateView) :
    login_url = '/home/login'
    redirect_field_name = ''
    model = Blog
    template_name = 'blog/addBlog.html'
    fields = ['title', 'content']
    success_url = '/home/'

