from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add_blog/$', AddBlog.as_view(), name='add_blog'),
]