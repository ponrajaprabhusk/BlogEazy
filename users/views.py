from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile
from .forms import CustomUserCreationForm , ProfileForm

# Create your views here.
@login_required(login_url='login')
def profile_page(request):
    profile = request.user.profile

    context = { 'profile': profile }
    return render(request, 'users/profile_page.html', context)

@login_required(login_url='login')
def update_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('users')

    context = {'form': form}
    return render(request, 'users/update_profile.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')    

        user = authenticate(request, username = username, password = password)
        if user is not None:
                login(request, user)
                return redirect('')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context ={}
    return render(request, 'users/login.html', context)    

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('')

    register_form = CustomUserCreationForm()
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit =False)
            user.username = user.username.lower()
            user.save()
            messages.info(request, "Account created successfully")
            login(request, user)
            return redirect('')

    context = {'register_form':register_form}        
    return render(request, 'users/register.html', context)    