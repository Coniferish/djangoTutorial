from django.shortcuts import render
from django.http import HttpResponse

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
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return HttpResponse('<h1>About</h1>')