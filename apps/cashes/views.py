from django.shortcuts import render, redirect
from .models import Cash, InCash, InCashClient, OutCash, Expense, Transaction, OutCashClient
from django.http import HttpResponseRedirect
from .forms import CashForm, InCashForm, InCashClientForm, OutCashForm, ExpenseForm, OutCashClientForm
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
            return redirect('cash_list')
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
            form.save()
            return redirect('in_cash_list')
    else:
        form = InCashForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_in_cash.html',context )

def update_in_cash(request, id):
    cash = InCash.objects.get(pk=id)
    form = InCashForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():

        form.save()
        return redirect('in_cash_list')
    return render(request, 'cashes/update_in_cash.html', {
       'form': form,
       'cash': cash,
    })

def delete_in_cash(request, id):
    cash = InCash.objects.get(pk=id)
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
            form.save()
            return redirect('in_cashclient_list')
    else:
        form = InCashClientForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_in_cashclient.html',context )

def update_in_cashclient(request, id):
    cash = InCashClient.objects.get(pk=id)
    form = InCashClientForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():

        form.save()
        return redirect('in_cashclient_list')
    return render(request, 'cashes/update_in_cashclient.html', {
       'form': form,
       'cash': cash,
    })

def delete_in_cashclient(request, id):
    cash = InCashClient.objects.get(pk=id)
    cash.delete()
    return redirect('in_cashclient_list')


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
            # t = form.cleaned_data['trader']
            # c = form.cleaned_data['cash']
            # s = int(form.cleaned_data['summa'])
            # comment = form.cleaned_data['comment']
            # date = form.cleaned_data['out_date']
            # qs = Transaction.objects.all()
            # qs.create(trans_date = date, comment = comment, provider = t, cash = c, cash_summa = s)

            # trader = User.objects.filter(user_type = 'PR').get(username=t)
            # trader.balance -= s
            # trader.save()

            # cash = Cash.objects.get(name=c)
            # cash.balance -= s
            # cash.save()

            form.save()
            return redirect('out_cash_list')
    else:
        form = OutCashForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_out_cash.html',context )

def update_out_cash(request, id):
    cash = OutCash.objects.get(pk=id)
    form = OutCashForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():

        form.save()
        return redirect('out_cash_list')
    return render(request, 'cashes/update_out_cash.html', {
       'form': form,
       'cash': cash,
    })

def delete_out_cash(request, id):
    cash = OutCash.objects.get(pk=id)
    cash.delete()
    return redirect('out_cash_list')


# Pul chiqimi Client
def out_cashClient_list(request):
    out_cashClient_list = OutCashClient.objects.all().order_by('-out_date')
    return render(request, 'cashes/out_cashClient_list.html', {
        'out_cashClient_list' : out_cashClient_list,
    })

def add_out_cashClient(request):
    submitted = False
    if request.method == "POST":
        form = OutCashClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('out_cashClient_list')
    else:
        form = OutCashClientForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_out_cashClient.html',context )

def update_out_cashClient(request, id):
    cash = OutCashClient.objects.get(pk=id)
    form = OutCashClientForm(request.POST or None, request.FILES or None, instance=cash)
    if form.is_valid():

        form.save()
        return redirect('out_cashClient_list')
    return render(request, 'cashes/update_out_cashClient.html', {
       'form': form,
       'cash': cash,
    })

def delete_out_cashClient(request, id):
    cash = OutCashClient.objects.get(pk=id)
    cash.delete()
    return redirect('out_cashClient_list')


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

            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'cashes/add_expense.html',context )

def update_expense(request, id):
    exp = Expense.objects.get(pk=id)
    form = ExpenseForm(request.POST or None, request.FILES or None, instance=exp)
    if form.is_valid():

        form.save()
        return redirect('expense_list')
    return render(request, 'cashes/update_expense.html', {
       'form': form,
       'exp': exp,
    })

def delete_expense(request, id):
    exp = Expense.objects.get(pk=id)
    exp.delete()
    return redirect('expense_list')
