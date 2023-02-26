from django.shortcuts import render, redirect
from .models import InProduct, Product, Warehouse, OutProduct
from .forms import ProductForm, InProductForm, OutProductForm
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Max, Min, Sum
from apps.accounts.models import User
from apps.cashes.models import Transaction
from django.views import View

# Create your views here.

# Tovar kirimi
def in_product_list(request):
    in_product_list = InProduct.objects.all().order_by('-in_date')
    return render(request, 'products/in_product_list.html', {
        'in_product_list' : in_product_list,
    })

def add_in_product(request):
    submitted = False
    if request.method == "POST":
        form = InProductForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data['provider']
            bs = int(form.cleaned_data['body_summa'])
            comment = form.cleaned_data['comment']
            date = form.cleaned_data['in_date']
            qs = Transaction.objects.all()
            qs.create(trans_date = date, comment = comment, provider = p, body_summa = bs)

            provider = User.objects.filter(user_type = 'PR').get(username=p)
            provider.balance += bs
            provider.save()

            form.save()
            return HttpResponseRedirect('/products/add_in_product?submitted=True')
    else:
        form = InProductForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'sana' : form['in_date'],
        'kontragent' : form['provider'],
        'ombor' : form['warehouse'],
        'tovar' : form['product'],
        'soni' : form['quantity'],
        'tannarxi' : form['body_price'],
        'tansumma' : form['body_summa'],
        'narxi' : form['price'],
        'summa' : form['summa'],
        'snarxi' : form['shop_price'],
        'ssumma' : form['shop_summa'],
        'izoh' : form['comment'],
    }

    return render(request, 'products/add_in_product.html',context )

def update_in_product(request, product_id):
    product = InProduct.objects.get(pk=product_id)
    form = InProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        # p = form.cleaned_data['provider']
        # ts = int(form.cleaned_data['body_summa'])

        # provider = User.objects.filter(user_type = 'PR').get(username=p)
        # provider.balance = ts
        # provider.save()

        form.save()
        return redirect('in_product_list')
    return render(request, 'products/update_in_product.html', {
       'form': form,
       'product': product,
    })

def delete_in_product(request, product_id):
    product = InProduct.objects.get(pk=product_id)
    product.delete()
    return redirect('in_product_list')


# Tovar chiqimi
def out_product_list(request):
    out_product_list = OutProduct.objects.all().order_by('-out_date')
    return render(request, 'products/out_product_list.html', {
        'out_product_list' : out_product_list,
    })

def add_out_product(request):
    submitted = False
    if request.method == "POST":
        form = OutProductForm(request.POST)
        if form.is_valid():
            t = form.cleaned_data['trader']
            c = form.cleaned_data['client']
            s = int(form.cleaned_data['summa'])
            ss = int(form.cleaned_data['shop_summa'])
            comment = form.cleaned_data['comment']
            date = form.cleaned_data['out_date']
            qs = Transaction.objects.all()
            qs.create(trans_date = date, comment = comment, provider = t, client = c, summa = s, shop_summa = ss)
            # p = form.cleaned_data['product']
            # q= form.cleaned_data['quantity']
            # w= form.cleaned_data['warehouse']
            # bs = int(form.cleaned_data['body_summa'])

            # product = InProduct.objects.filter(warehouse=w, product=p)
            # product.quantity -= q
            # product.body_summa -= bs
            # product.save()
            
            trader = User.objects.filter(user_type = 'PR').get(username=t)
            trader.balance -= s
            trader.save()

            client = User.objects.filter(user_type = 'CL').get(username=c)
            client.balance -= ss
            client.save()

            form.save()
            return HttpResponseRedirect('/products/add_out_product?submitted=True')
    else:
        form = OutProductForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'sana' : form['out_date'],
        'trader' : form['trader'],
        'client' : form['client'],
        'ombor' : form['warehouse'],
        'tovar' : form['product'],
        'soni' : form['quantity'],
        'tannarxi' : form['body_price'],
        'tansumma' : form['body_summa'],
        'narxi' : form['price'],
        'summa' : form['summa'],
        'snarxi' : form['shop_price'],
        'ssumma' : form['shop_summa'],
        'foyda' : form['profit'],
        'sfoyda' : form['sprofit'],
        'izoh' : form['comment'],
    }

    return render(request, 'products/add_out_product.html',context )

def update_out_product(request, product_id):
    product = OutProduct.objects.get(pk=product_id)
    form = OutProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
            form.save()
            return redirect('out_product_list')
    return render(request, 'products/update_out_product.html', {
       'form': form,
       'product': product,
    })

def delete_out_product(request, product_id):
    product = OutProduct.objects.get(pk=product_id)
    product.delete()
    return redirect('out_product_list')


# Ombor
def warehouse(request):
    warehouses = Warehouse.objects.all()
    data = []
    
    if request.method == "POST":
        selected = request.POST['selected']
        qs = InProduct.objects.filter(warehouse__name=selected)
        
        for item in qs:
            name = item.product.name
            if name in [x['name'] for x in data]:
                for x in data:     
                    if x['name'] == name:
                        x['total_soni'] += item.quantity
                        x['total_sum'] += item.body_summa
                        # x['total_narxi'] += item.body_summa/item.quantity
                        x['total_size'] += item.product.product_size
                        x['total_weight'] += item.product.product_weight
            else:
                data.append({
                    "id": item.id,
                    "name": item.product.name,
                    "total_soni": item.quantity,
                    "total_narxi": item.body_price,
                    "total_sum": item.body_summa,
                    "total_size": item.product.product_size,
                    "total_weight": item.product.product_weight,
                    })
        size = Warehouse.objects.filter(name=selected).values()

        return render(request, 'products/warehouse.html', {
            'warehouses': warehouses,
            'selected' : selected,
            'results': data,
            'size' : size,
        })
    else:
        return render(request, 'products/warehouse.html', {'warehouses': warehouses, 'results': data,})


# Tovar hosil qilish
def product_name_list(request):
    product_list = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'product_list' : product_list,
    })

def add_product_name(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_product_name?submitted=True')
    else:
        form = ProductForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products/add_product_name.html', {
        'form': form,
       'submitted': submitted
    })

def update_product_name(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'products/update_product_name.html', {
       'form': form,
       'product': product,
    })

def delete_product_name(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product_list')

