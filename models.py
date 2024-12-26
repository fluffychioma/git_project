from django.db import models
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

class Post(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.author)
