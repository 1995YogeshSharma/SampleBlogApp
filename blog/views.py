from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
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

class DetailBlog(DetailView) :
    template_name = 'blog/view_single_blog.html'

    def get_queryset(self, **kwargs):
        queryset = Blog.objects.filter(pk=self.kwargs['pk'])
        return queryset

class AuthorBlog(LoginRequiredMixin, ListView) :
    template_name = 'blog/view_author_blogs.html'
    login_url = '/home/login'
    redirect_field_name = ''
    def get_queryset(self, **kwargs):
        queryset = Blog.objects.filter(author=self.request.user.id)
        return queryset
