from django.shortcuts import render, redirect
from .models import Cash, InCash, InCashClient, OutCash, Expense
from django.http import HttpResponseRedirect
from .forms import CashForm, InCashForm, InCashClientForm, OutCashForm, ExpenseForm
from apps.accounts.models import User

# Create your views here.


# Kassa hosil qilish
def cash_name_list(request):
    cash_list = Cash.objects.all()
    return render(request, 'cashes/cash_list.html', {
        'cash_list' : cash_list,
    })

def add_cash_name(request):
    submitted = False
    if request.method == "POST":
        form = CashForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_cash_name?submitted=True')
    else:
        form = CashForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'cashes/add_cash_name.html', {
        'form': form,
       'submitted': submitted
    })

def update_cash_name(request, cash_id):
    cash = Cash.objects.get(pk=cash_id)
    form = CashForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():
            form.save()
            return redirect('cash_list')
    return render(request, 'cashes/update_cash_name.html', {
       'form': form,
       'cash': cash,
    })

def delete_cash_name(request, cash_id):
    cash = Cash.objects.get(pk=cash_id)
    cash.delete()
    return redirect('cash_list')


# Pul kirimi
def in_cash_list(request):
    in_cash_list = InCash.objects.all().order_by('-in_date')
    return render(request, 'cashes/in_cash_list.html', {
        'in_cash_list' : in_cash_list,
    })

def add_in_cash(request):
    submitted = False
    if request.method == "POST":
        form = InCashForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['trader']
            c = form.cleaned_data['cash']
            s = int(form.cleaned_data['summa'])

            trader = User.objects.filter(user_type = 'PR').get(username=t)
            trader.balance += s
            trader.save()

            cash = Cash.objects.get(name=c)
            cash.balance += s
            cash.save()

            form.save()
            return HttpResponseRedirect('/cashes/add_in_cash?submitted=True')
    else:
        form = InCashForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_in_cash.html',context )

def update_in_cash(request, cash_id):
    cash = InCash.objects.get(pk=cash_id)
    form = InCashForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():
        # p = form.cleaned_data['provider']
        # ts = int(form.cleaned_data['body_summa'])

        # provider = User.objects.filter(user_type = 'PR').get(username=p)
        # provider.balance = ts
        # provider.save()

        form.save()
        return redirect('in_cash_list')
    return render(request, 'cashes/update_in_cash.html', {
       'form': form,
       'cash': cash,
    })

def delete_in_cash(request, cash_id):
    cash = InCash.objects.get(pk=cash_id)
    cash.delete()
    return redirect('in_cash_list')


# Pul kirimi client
def in_cashclient_list(request):
    in_cashclient_list = InCashClient.objects.all().order_by('-in_date')
    return render(request, 'cashes/in_cashclient_list.html', {
        'in_cashclient_list' : in_cashclient_list,
    })

def add_in_cashclient(request):
    submitted = False
    if request.method == "POST":
        form = InCashClientForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data['client']
            s = int(form.cleaned_data['summa'])

            client = User.objects.filter(user_type = 'CL').get(username=c)
            client.balance += s
            client.save()

            form.save()
            return HttpResponseRedirect('/cashes/add_in_cashclient?submitted=True')
    else:
        form = InCashClientForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_in_cashclient.html',context )

# def update_in_cashclient(request, incash_id):
#     cash = InCashClient.objects.get(pk=incash_id)
#     form = InCashClientForm(request.POST or None, request.FILES or None, instance=cash)
#     if form.is_valid():
#         # p = form.cleaned_data['provider']
#         # ts = int(form.cleaned_data['body_summa'])

#         # provider = User.objects.filter(user_type = 'PR').get(username=p)
#         # provider.balance = ts
#         # provider.save()

#         form.save()
#         return redirect('in_cashclient_list')
#     return render(request, 'cashes/update_in_cashclient.html', {
#        'form': form,
#        'cash': cash,
#     })

# def delete_in_cashclient(request, web):
#     cashclient = InCashClient.objects.get(pk=web)
#     cashclient.delete()
#     return redirect('in_cashclient_list')


# Pul chiqimi
def out_cash_list(request):
    out_cash_list = OutCash.objects.all().order_by('-out_date')
    return render(request, 'cashes/out_cash_list.html', {
        'out_cash_list' : out_cash_list,
    })

def add_out_cash(request):
    submitted = False
    if request.method == "POST":
        form = OutCashForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['trader']
            c = form.cleaned_data['cash']
            s = int(form.cleaned_data['summa'])

            trader = User.objects.filter(user_type = 'PR').get(username=t)
            trader.balance -= s
            trader.save()

            cash = Cash.objects.get(name=c)
            cash.balance -= s
            cash.save()

            form.save()
            return HttpResponseRedirect('/cashes/add_out_cash?submitted=True')
    else:
        form = OutCashForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_out_cash.html',context )

def update_out_cash(request, cash_id):
    cash = OutCash.objects.get(pk=cash_id)
    form = OutCashForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():
        # p = form.cleaned_data['provider']
        # ts = int(form.cleaned_data['body_summa'])

        # provider = User.objects.filter(user_type = 'PR').get(username=p)
        # provider.balance = ts
        # provider.save()

        form.save()
        return redirect('out_cash_list')
    return render(request, 'cashes/update_out_cash.html', {
       'form': form,
       'cash': cash,
    })

def delete_out_cash(request, cash_id):
    cash = OutCash.objects.get(pk=cash_id)
    cash.delete()
    return redirect('out_cash_list')


# Xarajat
def expense_list(request):
    expense_list = Expense.objects.all().order_by('-date')
    return render(request, 'cashes/expense_list.html', {
        'expense_list' : expense_list,
    })

def add_expense(request):
    submitted = False
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data['cash']
            s = int(form.cleaned_data['summa'])

            cash = Cash.objects.get(name=c)
            cash.balance -= s
            cash.save()

            form.save()
            return HttpResponseRedirect('/cashes/add_expense?submitted=True')
    else:
        form = ExpenseForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_expense.html',context )

# def update_expense(request, cash_id):
#     cash = Expense.objects.get(pk=cash_id)
#     form = ExpenseForm(request.POST or None, request.FILES or None, instance=cash)
#     if form.is_valid():
#         # p = form.cleaned_data['provider']
#         # ts = int(form.cleaned_data['body_summa'])

#         # provider = User.objects.filter(user_type = 'PR').get(username=p)
#         # provider.balance = ts
#         # provider.save()

#         form.save()
#         return redirect('expense_list')
#     return render(request, 'cashes/update_expense.html', {
#        'form': form,
#        'cash': cash,
#     })

# def delete_expense(request, cash_id):
#     cash = Expense.objects.get(pk=cash_id)
#     cash.delete()
#     return redirect('expense_list')