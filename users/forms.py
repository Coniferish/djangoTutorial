from django import forms # https://docs.djangoproject.com/en/4.1/topics/forms/
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/4.1/topics/auth/default/
from django.contrib.auth.forms import UserCreationForm 
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    # create fields we want to add to the UserCreationForm
    email = forms.EmailField()
    
    # https://docs.djangoproject.com/en/4.1/topics/db/models/#meta-options
    # https://docs.djangoproject.com/en/4.1/ref/models/meta/
    # https://code.djangoproject.com/wiki/DevModelCreation#ImportingAModel
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        