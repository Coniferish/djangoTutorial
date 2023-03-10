from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# https://docs.djangoproject.com/en/4.1/topics/class-based-views/
# https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
class PostListView(ListView):
    # class views generally cut down on code and consist of simply defining attributes (more simple)
    model = Post
    # class based views look for templates with a certain naming pattern:
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    # this class view also needs to know the variable name for the items it will be iterating over
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    # for this class view, we're using the django defaults, 
    # so we aren't defining the template_name, context_object_name, etc.
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
