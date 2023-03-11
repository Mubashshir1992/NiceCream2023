from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreateonForm
from .models import User
from apps.cashes.models import Transaction
from apps.products.models import InDocument
import datetime

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
    
    providers = User.objects.exclude(balance = 0).filter(user_type = 'PR')
    return render(request, 'accounts/providers.html', {
        'providers' : providers,
    })

# Clientlar
def clients(request):
    clients = User.objects.exclude(balance = 0).filter(user_type = 'CL')
    return render(request, 'accounts/clients.html', {
        'clients' : clients,
    })


# Akt sverka Provider
def act_sverka(request):
        providers = User.objects.filter(user_type = 'PR')
        provider = None
        todate = None
        fromdate = None
        qs = None
        if request.method == "POST":
            provider = request.POST['provider']
            fromdate = request.POST['fromdate']
            todate = request.POST['todate']
            qs = Transaction.objects.filter(provider__username=provider, trans_date__lte = todate, trans_date__gte = fromdate,)

        return render(request, 'accounts/act_sverka.html', {
        'providers' : providers,
        'provider' : provider,
        'todate' : todate,
        'fromdate' : fromdate,
        'qs' : qs,

    })


 # Akt sverka Client
def act_sverka_client(request):
        clients = User.objects.filter(user_type = 'CL')
        client = None
        todate = None
        fromdate = None
        qs = None
        if request.method == "POST":
            client = request.POST['client']
            fromdate = request.POST['fromdate']
            todate = request.POST['todate']
            qs = Transaction.objects.filter(client__username=client, trans_date__lte = todate, trans_date__gte = fromdate,)

        return render(request, 'accounts/act_sverka_client.html', {
        'clients' : clients,
        'client' : client,
        'todate' : todate,
        'fromdate' : fromdate,
        'qs' : qs,

    })  


# MY Akt sverka
def my_act_sverka(request):
        me = request.user.id
        document_list = InDocument.objects.all()
        for doc in document_list:
            document=doc
            
        pr_id = User.objects.filter(user_type = 'PR').values_list('id', flat=True)
        cl_id = User.objects.filter(user_type = 'CL').values_list('id', flat=True)
        today = datetime.date.today()
        todate = today + datetime.timedelta(days=1)
        fromdate = today.replace(day=1)
        if me in pr_id:
            qs = Transaction.objects.filter(provider_id=me, trans_date__lte = todate, trans_date__gte = fromdate,)
        if me in cl_id:
            qs = Transaction.objects.filter(client_id=me, trans_date__lte = todate, trans_date__gte = fromdate,)
            
        if request.method == "POST":
            fromdate = request.POST['fromdate']
            todate = request.POST['todate']
            if me in pr_id:
                qs = Transaction.objects.filter(provider_id=me, trans_date__lte = todate, trans_date__gte = fromdate,)
            if me in cl_id:
                qs = Transaction.objects.filter(client_id=me, trans_date__lte = todate, trans_date__gte = fromdate,)

        return render(request, 'accounts/my_act_sverka.html', {
        'todate' : todate,
        'fromdate' : fromdate,
        'qs' : qs,
        'document' : document,

    })  