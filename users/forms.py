from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email', 'password1', 'password2' ]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email','location', 'bio', 'short_intro', 'profile_image','social_github', 'social_linkedin', 'social_twitter','social_youtube', 'social_website']
