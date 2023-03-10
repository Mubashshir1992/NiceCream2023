from django import forms
from django.forms.widgets import NumberInput
from django.forms import ModelForm
from .models import Product, InProduct, OutProduct, OutProductB, WarehouseName, InDocument, OutDocument, OutDocumentClient


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'capacity', 'brand', 'product_size', 'product_weight', 'code', 'image' , 'price', 's_price' , 'about')

        labels = {
            'name': '',
            'capacity': '',
            'brand': '',
            'product_size' : '',
            'product_weight' : '',
            'code': '',
            'image': 'Tovar rasmi',
            'about': '',
            'price': '',
            's_price': '',
            }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mahsulot nomi'}),
            'capacity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quti sig`imi'}),
            'brand': forms.Select(attrs={'class':'form-control', 'placeholder':'Brand nomi'}),
            'product_size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tovar hajmi'}),
            'product_weight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tovar og`irligi'}),
            'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mahsulot kodi'}),
            'about': forms.Textarea(attrs={'rows':3,'class':'form-control', 'placeholder':'Mahsulot haqida'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tavsiya narxi'}),
            's_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tavsiya snarxi'}),
        }


class InProductForm(ModelForm):
    class Meta:
        model = InProduct
        fields = ('document', 'product', 'quantity', 'body_price', 'body_summa', 'price', 'summa', 'shop_price', 'shop_summa')

        labels = {
            'document' : '',
            'product' : '',
            'quantity' : '',
            'body_price' : '',
            'body_summa' : '',
            'price' : '',
            'summa' : '',
            'shop_price' : '',
            'shop_summa' : '',
            }
        
        widgets = {
            'document': forms.Select(attrs={'class':'form-control', 'placeholder':'Document nomi'}),
            'product': forms.Select(attrs={'class':'form-control', 'placeholder':'Mahsulot nomi'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Soni'}),
            'body_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanNarxi'}),
            'body_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanSumma'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Narxi'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'shop_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Snarxi'}),
            'shop_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ssumma'}),
        }


class OutProductForm(ModelForm):

    class Meta:
        model = OutProduct
        fields = ('document', 'product', 'quantity', 'body_price', 'body_summa', 'price', 'summa', 'profit',)

        labels = {
            'document' : '',
            'product' : '',
            'quantity' : '',
            'body_price' : '',
            'body_summa' : '',
            'price' : '',
            'summa' : '',
            'profit' : '',
            }
        
        widgets = {
            'document': forms.Select(attrs={'class':'form-control', 'placeholder':'Document nomi'}),
            'product': forms.Select(attrs={'class':'form-control', 'placeholder':'Mahsulot nomi'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Soni'}),
            'body_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanNarxi'}),
            'body_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanSumma'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Narxi'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'profit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Foyda'}),
        }


class OutProductBForm(ModelForm):

    class Meta:
        model = OutProductB
        fields = ('document', 'product', 'quantity', 'body_price', 'body_summa', 'price', 'summa', 'shop_price', 'shop_summa', 'profit', 'sprofit')

        labels = {
            'document' : '',
            'product' : '',
            'quantity' : '',
            'body_price' : '',
            'body_summa' : '',
            'price' : '',
            'summa' : '',
            'shop_price' : '',
            'shop_summa' : '',
            'profit' : '',
            'sprofit' : '',
            }
        
        widgets = {
            'document': forms.Select(attrs={'class':'form-control', 'placeholder':'Document nomi'}),
            'product': forms.Select(attrs={'class':'form-control', 'placeholder':'Mahsulot nomi'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Soni'}),
            'body_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanNarxi'}),
            'body_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanSumma'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Narxi'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'shop_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Snarxi'}),
            'shop_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ssumma'}),
            'profit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Foyda'}),
            'sprofit': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sfoyda'}),
        }


class WarehouseNameForm(ModelForm):
    class Meta:
        model = WarehouseName
        fields = ('name', 'warehouse_size',)

        labels = {
            'name': '',
            'warehouse_size': '',
            }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ombor nomi'}),
            'warehouse_size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ombor hajmi'}),
        }

class InDocumentForm(ModelForm):
    class Meta:
        model = InDocument
        fields = ('in_date', 'warehouse', 'provider', 'comment')

        labels = {
            'in_date': 'YYYY-MM-DD HH:MM:SS',
            'warehouse': 'Ombor',
            'provider': 'Provider',
            'comment' : '',
            }
        
        widgets = {
            'in_date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'warehouse': forms.Select(attrs={'class':'form-control', 'placeholder':'Ombor'}),
            'provider': forms.Select(attrs={'class':'form-control', 'placeholder':'Provider'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }

class OutDocumentForm(ModelForm):
    class Meta:
        model = OutDocument
        fields = ('out_date', 'warehouse', 'trader', 'comment')

        labels = {
            'out_date': 'YYYY-MM-DD HH:MM:SS',
            'warehouse': 'Ombor',
            'trader': 'Trader',
            'comment' : '',
            }
        
        widgets = {
            'out_date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'warehouse': forms.Select(attrs={'class':'form-control', 'placeholder':'Ombor'}),
            'trader': forms.Select(attrs={'class':'form-control', 'placeholder':'Trader'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }

class OutDocumentClientForm(ModelForm):
    class Meta:
        model = OutDocumentClient
        fields = ('out_date', 'warehouse', 'trader', 'client', 'comment')

        labels = {
            'out_date': 'YYYY-MM-DD HH:MM:SS',
            'warehouse': 'Ombor',
            'trader': 'Trader',
            'client': 'Client',
            'comment' : '',
            }
        
        widgets = {
            'out_date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'warehouse': forms.Select(attrs={'class':'form-control', 'placeholder':'Ombor'}),
            'trader': forms.Select(attrs={'class':'form-control', 'placeholder':'Trader'}),
            'client': forms.Select(attrs={'class':'form-control', 'placeholder':'Client'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }

