from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_on = models.DateTimeField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title + "  -  " + self.author.username
