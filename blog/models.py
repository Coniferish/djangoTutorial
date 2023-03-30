from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # We use "reverse" instead of "redirect" method because "reverse"
        # returns a string. We want this because the view will handle the redirect.
        # We use 'pk' because that's the default for django.views.generic (views)
        return reverse('post-detail', kwargs={'pk': self.pk})
        