from django.views.generic import CreateView, ListView, DetailView

from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from django.db.models import Avg

from .models import Blog, Rating

from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime


class AddBlog(LoginRequiredMixin, CreateView):
    """
    allowed logged in user to add a blog
    """
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
    """
    allows user to browse through all the blogs
    """
    template_name = 'blog/view_all_blogs.html'
    model = Blog


class DetailBlog(DetailView) :
    """
    allows user to view single blog
    """
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
    """
    allows user to view his blogs
    """
    template_name = 'blog/view_author_blogs.html'
    login_url = '/home/login'
    redirect_field_name = ''

    def get_queryset(self, **kwargs):
        queryset = Blog.objects.filter(author=self.request.user.id)
        return queryset


@login_required
def RateBlog(request, pk):
    """
    allows logged in user to rate a blog ( responds to ajax call by the user )
    """
    blog = Blog.objects.get(pk=pk)

    #checking if already rated
    if Rating.objects.filter(blog_name=blog, rated_by_id=request.user.id).exists() :
        return HttpResponse('already rated')

    print request.GET.get('rating', False)

    new_rating = Rating.objects.create(blog_name=blog, rated_by_id=request.user.id, rating=int(request.GET.get('rating', False)))

    new_rating.save()

    return HttpResponse('ratings added')

