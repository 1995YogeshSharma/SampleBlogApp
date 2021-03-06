from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

# Create your models here.
class Blog(models.Model):
    """
    model to store the details about the blogs
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = tinymce_models.HTMLField()
    created_on = models.DateTimeField()

    def __str__(self):
        return self.title + "  -  " + self.author.username


class Rating(models.Model):
    """
    model to store the ratings given by users
    """
    blog_name = models.ForeignKey(Blog, on_delete=models.CASCADE)
    rated_by_id = models.IntegerField()
    rating = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)), default=0)

    class Meta():
        unique_together = (("blog_name", "rated_by_id"),)

    def __str__(self):
        return self.blog_name.title + " rated by id " + str(self.rated_by_id)