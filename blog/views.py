from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Buggs Bunny',
        'title': 'Carrots?',
        'content': 'Carrots are great.',
        'date_posted': '20230215',
    },
    {
        'author': 'Tommy Pickles',
        'title': 'Crayons?',
        'content': 'Crayons are great.',
        'date_posted': '20230214',
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})