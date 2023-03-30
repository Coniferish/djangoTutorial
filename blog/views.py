from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/
# https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
class PostListView(ListView):
    # class views generally cut down on code and consist of simply defining attributes (more simple)
    model = Post
    # class based views look for templates with a certain naming pattern:
    # <app>/<model>_<viewtype>.html
    # but you can override this:
    template_name = 'blog/home.html'
    # this class view also needs to know the variable name for the items it will be iterating over
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    # for this class view, we're using the django defaults, 
    # so we aren't defining the template_name, context_object_name, etc. (as done above)
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    # because we're going to share the template for this view, 
    # django expects the name to be <model>_form, so "post_form" is the template name
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
