from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):

    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blob_posts', null=True, on_delete=models.SET_NULL)
    body = models.TextField()
    publish = models.DateTimeField(timezone.now)

    class Mata:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
