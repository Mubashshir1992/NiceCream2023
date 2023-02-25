from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreateonForm
from .models import User

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again... "))
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreateonForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = CustomUserCreateonForm()        
    return render(request, 'registration/register_user.html', {
        'form': form,
    })



# optomchilar
def providers(request):
    
    providers = User.objects.filter(user_type = 'PR')
    return render(request, 'accounts/providers.html', {
        'providers' : providers,
    })

# Clientlar
def clients(request):
    clients = User.objects.filter(user_type = 'CL')
    return render(request, 'accounts/clients.html', {
        'clients' : clients,
    })