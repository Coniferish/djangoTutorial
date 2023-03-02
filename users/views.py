from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# https://docs.djangoproject.com/en/4.1/topics/auth/
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms
# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # this automatically hashes the password and everything else
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
