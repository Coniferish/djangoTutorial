from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# https://docs.djangoproject.com/en/4.1/topics/auth/
# https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms
# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() # this automatically hashes the password and everything else
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You may now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account successfully updated!')
            return redirect('profile') # add this to avoid the "post, get, redirect" pattern
            # i.e. where a user tries to reload a page and gets a warning about reloading it
            # this occurs because the user is inadvertently trying to send another POST request instead of a GET
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        # create a context that will be passed into the template
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
