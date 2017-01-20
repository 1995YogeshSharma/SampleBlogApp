from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
# Create your views here.

class AddBlog(LoginRequiredMixin, CreateView) :
    login_url = '/home/login'
    redirect_field_name = ''
    model = Blog
    template_name = 'blog/addBlog.html'
    fields = ['title', 'content']
    success_url = '/home/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_on = datetime.now()
        form.instance.rating = 0
        return super(AddBlog, self).form_valid(form)

class ViewAll(ListView) :
    template_name = 'blog/view_all_blogs.html'
    model = Blog

