from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from django.db.models import Avg

from .models import Blog
from .models import Rating
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
    # rating to be passed also in this view
    template_name = 'blog/view_all_blogs.html'
    model = Blog


class DetailBlog(DetailView) :
    template_name = 'blog/view_single_blog.html'

    def get_queryset(self, **kwargs):
        queryset = Blog.objects.filter(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DetailBlog, self).get_context_data(**kwargs)
        obj = Blog.objects.get(pk=self.kwargs['pk'])
        rating = Rating.objects.filter(blog_name__title=obj.title)
        context['rating'] = rating.aggregate(Avg('rating'))
        return context


class AuthorBlog(LoginRequiredMixin, ListView) :
    template_name = 'blog/view_author_blogs.html'
    login_url = '/home/login'
    redirect_field_name = ''

    def get_queryset(self, **kwargs):
        queryset = Blog.objects.filter(author=self.request.user.id)
        return queryset

@login_required
def RateBlog(request, pk):
    blog = Blog.objects.get(pk=pk)

    #checking if already rated
    if Rating.objects.filter(blog_name=blog, rated_by_id=request.user.id).exists() :
        return HttpResponse('already rated')

    print request.GET.get('rating', False)

    new_rating = Rating.objects.create(blog_name=blog, rated_by_id=request.user.id, rating=int(request.GET.get('rating', False)))

    new_rating.save()

    return HttpResponse('ratings added')

