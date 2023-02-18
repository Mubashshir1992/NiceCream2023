from django import forms
from django.forms import ModelForm
from .models import Product, InProduct

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'capacity', 'brand', 'product_size', 'product_weight', 'code', 'image')

        labels = {
            'name': '',
            'capacity': '',
            'brand': '',
            'product_size' : '',
            'product_weight' : '',
            'code': '',
            'image': 'Tovar rasmi',
            }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mahsulot nomi'}),
            'capacity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Quti sig`imi'}),
            'brand': forms.Select(attrs={'class':'form-control', 'placeholder':'Brand nomi'}),
            'product_size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tovar hajmi'}),
            'product_weight': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tovar og`irligi'}),
            'code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mahsulot kodi'}),
        }

class InProductForm(ModelForm):
    class Meta:
        model = InProduct
        fields = ('in_date', 'warehouse', 'provider', 'product', 'quantity', 'body_price', 'body_summa', 'price', 'summa', 'shop_price', 'shop_summa', 'comment')

        labels = {
            'in_date': 'YYYY-MM-DD HH:MM:SS',
            'warehouse': 'Ombor',
            'provider': 'Provider',
            'product' : '',
            'quantity' : '',
            'body_price' : '',
            'body_summa' : '',
            'price' : '',
            'summa' : '',
            'shop_price' : '',
            'shop_summa' : '',
            'comment' : '',
            }
        
        widgets = {
            'in_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sana'}),
            'warehouse': forms.Select(attrs={'class':'form-control', 'placeholder':'Ombor'}),
            'provider': forms.Select(attrs={'class':'form-control', 'placeholder':'Provider'}),
            'product': forms.Select(attrs={'class':'form-control', 'placeholder':'Mahsulot nomi'}),
            'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Soni'}),
            'body_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanNarxi'}),
            'body_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'TanSumma'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Narxi'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'shop_price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Snarxi'}),
            'shop_summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ssumma'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }