from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based views look for templates with a certain naming pattern:
# <app>/<model>_<viewtype>.html
# but we can change this default with "template_name"
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    # this class view also needs to know the variable name for the items it will be iterating over
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
