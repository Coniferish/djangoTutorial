from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# https://docs.djangoproject.com/en/4.1/topics/auth/
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
