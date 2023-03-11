from django.shortcuts import render, redirect
from .models import InProduct, Product, WarehouseName, OutProduct, OutProductB, Warehouse, InDocument, OutDocument, OutDocumentClient
from .forms import ProductForm, InProductForm, OutProductForm, OutProductBForm, WarehouseNameForm, InDocumentForm, OutDocumentForm, OutDocumentClientForm
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Max, Min, Sum
from apps.accounts.models import User
from apps.cashes.models import Transaction
from django.views import View
from django.contrib import messages

# Create your views here.

# Tovar kirimi
def in_product_list(request):
    in_product_list = InProduct.objects.all()
    return render(request, 'products/in_product_list.html', {
        'in_product_list' : in_product_list,
    })

def add_in_product(request):
    submitted = False
    if request.method == "POST":
        form = InProductForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('in_product_list')
    else:
        form = InProductForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'document' : form['document'],
        'tovar' : form['product'],
        'soni' : form['quantity'],
        'tannarxi' : form['body_price'],
        'tansumma' : form['body_summa'],
        'narxi' : form['price'],
        'summa' : form['summa'],
        'snarxi' : form['shop_price'],
        'ssumma' : form['shop_summa'],
    }

    return render(request, 'products/add_in_product.html',context )

def update_in_product(request, product_id):
    product = InProduct.objects.get(pk=product_id)
    form = InProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():

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
    out_product_list = OutProduct.objects.all()
    return render(request, 'products/out_product_list.html', {
        'out_product_list' : out_product_list,
    })

def add_out_product(request):
    
    initial_date={
        'body_price':'',
        'price':'',
    }
    submitted = False
    if request.method == "POST":
        form = OutProductForm(request.POST)
        if form.is_valid():
           
            form.save()
            return HttpResponseRedirect('/products/out_product_list?submitted=True')
    else:
        form = OutProductForm(initial=initial_date)
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'document' : form['document'],
        'tovar' : form['product'],
        'soni' : form['quantity'],
        'tannarxi' : form['body_price'],
        'tansumma' : form['body_summa'],
        'narxi' : form['price'],
        'summa' : form['summa'],
        'foyda' : form['profit'],
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


# Tovar chiqimi B
def out_productb_list(request):
    out_product_list = OutProductB.objects.all()
    return render(request, 'products/out_productb_list.html', {
        'out_product_list' : out_product_list,
    })

def add_out_productb(request):
    submitted = False
    if request.method == "POST":
        form = OutProductBForm(request.POST)
        if form.is_valid():
           
            form.save()
            return HttpResponseRedirect('/products/out_productb_list?submitted=True')
    else:
        form = OutProductBForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'document' : form['document'],
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
    }

    return render(request, 'products/add_out_productb.html',context )

def update_out_productb(request, product_id):
    product = OutProductB.objects.get(pk=product_id)
    form = OutProductBForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
            form.save()
            return redirect('out_productb_list')
    return render(request, 'products/update_out_productb.html', {
       'form': form,
       'product': product,
    })

def delete_out_productb(request, product_id):
    product = OutProductB.objects.get(pk=product_id)
    product.delete()
    return redirect('out_productb_list')



# Ombor
def warehouse_name_list(request):
    warehouse_list = WarehouseName.objects.all()
    return render(request, 'products/warehouse_list.html', {
        'warehouse_list' : warehouse_list,
    })

def add_warehouse_name(request):
    submitted = False
    if request.method == "POST":
        form = WarehouseNameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    else:
        form = WarehouseNameForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products/add_warehouse_name.html', {
        'form': form,
       'submitted': submitted
    })

def update_warehouse_name(request, warehouse_id):
    warehouse = WarehouseName.objects.get(pk=warehouse_id)
    form = WarehouseNameForm(request.POST or None, request.FILES or None, instance=warehouse)
    if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    return render(request, 'products/update_warehouse_name.html', {
       'form': form,
       'warehouse': warehouse,
    })

def delete_warehouse_name(request, warehouse_id):
    warehouse = WarehouseName.objects.get(pk=warehouse_id)
    warehouse.delete()
    return redirect('warehouse_list')




def warehouse(request):
    warehouses = WarehouseName.objects.all()
    data = []
    
    if request.method == "POST":
        selected = request.POST['selected']
        qs = Warehouse.objects.filter(warehouse__name=selected)
        
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
        size = WarehouseName.objects.filter(name=selected).values()

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
            return redirect('product_list')
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

# def warehouseold(request):
#     warehouses = WarehouseName.objects.all()
#     data = []
    
#     if request.method == "POST":
#         selected = request.POST['selected']
#         qs = InProduct.objects.filter(warehouse__name=selected)
        
#         for item in qs:
#             name = item.product.name
#             if name in [x['name'] for x in data]:
#                 for x in data:     
#                     if x['name'] == name:
#                         x['total_soni'] += item.quantity
#                         x['total_sum'] += item.body_summa
#                         # x['total_narxi'] += item.body_summa/item.quantity
#                         x['total_size'] += item.product.product_size
#                         x['total_weight'] += item.product.product_weight
#             else:
#                 data.append({
#                     "id": item.id,
#                     "name": item.product.name,
#                     "total_soni": item.quantity,
#                     "total_narxi": item.body_price,
#                     "total_sum": item.body_summa,
#                     "total_size": item.product.product_size,
#                     "total_weight": item.product.product_weight,
#                     })
#         size = WarehouseName.objects.filter(name=selected).values()

#         return render(request, 'products/warehouse.html', {
#             'warehouses': warehouses,
#             'selected' : selected,
#             'results': data,
#             'size' : size,
#         })
#     else:
#         return render(request, 'products/warehouse.html', {'warehouses': warehouses, 'results': data,})


# InDocument hosil qilish

def in_document_list(request):
    document_list = InDocument.objects.all()
    return render(request, 'products/in_document_list.html', {
        'document_list' : document_list,
    })

def add_in_document(request):
    submitted = False
    if request.method == "POST":
        form = InDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('in_document_list')
    else:
        form = InDocumentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products/add_in_document.html', {
        'form': form,
       'submitted': submitted
    })

def update_in_document(request, document_id):
    document = InDocument.objects.get(pk=document_id)
    form = InDocumentForm(request.POST or None, request.FILES or None, instance=document)
    if form.is_valid():
            form.save()
            return redirect('in_document_list')
    return render(request, 'products/update_in_document.html', {
       'form': form,
       'document': document,
    })

def delete_in_document(request, document_id):
    document = InDocument.objects.get(pk=document_id)
    document.delete()
    return redirect('in_document_list')

def in_document_products(request, document_id):
    document = InDocument.objects.get(id=document_id)
    products = InProduct.objects.filter(document=document).values()
    

    if products:
        return render(request, 'products/in_document_products.html', {
            "products" : products,
        })
    else:
        messages.success(request, ("That Document Has No Products At This Time..!"))
        return redirect('in_document_list')


# OutDocument hosil qilish

def out_document_list(request):
    document_list = OutDocument.objects.all()
    return render(request, 'products/out_document_list.html', {
        'document_list' : document_list,
    })

def add_out_document(request):
    submitted = False
    if request.method == "POST":
        form = OutDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('out_document_list')
    else:
        form = OutDocumentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products/add_out_document.html', {
        'form': form,
       'submitted': submitted
    })

def update_out_document(request, document_id):
    document = OutDocument.objects.get(pk=document_id)
    form = OutDocumentForm(request.POST or None, request.FILES or None, instance=document)
    if form.is_valid():
            form.save()
            return redirect('out_document_list')
    return render(request, 'products/update_out_document.html', {
       'form': form,
       'document': document,
    })

def delete_out_document(request, document_id):
    document = OutDocument.objects.get(pk=document_id)
    document.delete()
    return redirect('out_document_list')

def out_document_products(request, document_id):
    document = OutDocument.objects.get(id=document_id)
    products = OutProduct.objects.filter(document=document).values()
    

    if products:
        return render(request, 'products/out_document_products.html', {
            "products" : products,
        })
    else:
        messages.success(request, ("That Document Has No Products At This Time..!"))
        return redirect('out_document_list')



# OutDocumentClient hosil qilish

def out_documentclient_list(request):
    document_list = OutDocumentClient.objects.all()
    return render(request, 'products/out_documentclient_list.html', {
        'document_list' : document_list,
    })

def add_out_documentclient(request):
    submitted = False
    if request.method == "POST":
        form = OutDocumentClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('out_documentclient_list')
    else:
        form = OutDocumentClientForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'products/add_out_documentclient.html', {
        'form': form,
       'submitted': submitted
    })

def update_out_documentclient(request, document_id):
    document = OutDocumentClient.objects.get(pk=document_id)
    form = OutDocumentClientForm(request.POST or None, request.FILES or None, instance=document)
    if form.is_valid():
            form.save()
            return redirect('out_documentclient_list')
    return render(request, 'products/update_out_documentclient.html', {
       'form': form,
       'document': document,
    })

def delete_out_documentclient(request, document_id):
    document = OutDocumentClient.objects.get(pk=document_id)
    document.delete()
    return redirect('out_documentclient_list')

def out_documentclient_products(request, document_id):
    document = OutDocumentClient.objects.get(id=document_id)
    products = OutProductB.objects.filter(document=document).values()
    

    if products:
        return render(request, 'products/out_documentclient_products.html', {
            "products" : products,
        })
    else:
        messages.success(request, ("That Document Has No Products At This Time..!"))
        return redirect('out_documentclient_list')
