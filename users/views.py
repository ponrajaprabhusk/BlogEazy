from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.
@login_required(login_url='login')
def profile_page(request):
    user = Profile.objects.all()
    context = { 'user': user }
    return render(request, 'profile_page.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('users')

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