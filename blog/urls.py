from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add_blog/$', AddBlog.as_view(), name='add_blog'),
    url(r'^view_all/$', ViewAll.as_view(), name='view_all'),
    url(r'^view_one/(?P<pk>\d+)', DetailBlog.as_view(), name='single_blog'),
    url(r'^author_blogs/$', AuthorBlog.as_view(), name='author_blog'),
]