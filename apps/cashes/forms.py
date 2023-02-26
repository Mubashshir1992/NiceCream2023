from django import forms
from django.forms import ModelForm
from .models import Cash, InCash, InCashClient, OutCash, Expense


class CashForm(ModelForm):
    class Meta:
        model = Cash
        fields = ('name', 'balance')

        labels = {
            'name': '',
            'balance': '',
            }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kassa nomi'}),
            'balance': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kassa qoldigi'}),
        }


class InCashForm(ModelForm):
    class Meta:
        model = InCash
        fields = ('in_date', 'trader', 'cash', 'summa', 'comment')

        labels = {
            'in_date': 'YYYY-MM-DD HH:MM:SS',
            'trader': 'Provider',
            'cash' : 'Cassa',
            'summa' : '',
            'comment' : '',
            }
        
        widgets = {
            'in_date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'trader': forms.Select(attrs={'class':'form-control', 'placeholder':'Provider'}),
            'cash': forms.Select(attrs={'class':'form-control', 'placeholder':'Cassa'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }

class InCashClientForm(ModelForm):
    class Meta:
        model = InCashClient
        fields = ('in_date', 'client', 'ssumma', 'comment')

        labels = {
            'in_date': 'YYYY-MM-DD HH:MM:SS',
            'client' : 'Client',
            'cash' : 'Cassa',
            'ssumma' : '',
            'comment' : '',
            }
        
        widgets = {
            'in_date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'client': forms.Select(attrs={'class':'form-control', 'placeholder':'Client'}),
            'ssumma': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SSumma'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }

class OutCashForm(ModelForm):
    class Meta:
        model = OutCash
        fields = ('out_date', 'trader', 'cash', 'summa', 'comment')

        labels = {
            'out_date': 'YYYY-MM-DD HH:MM:SS',
            'trader': 'Provider',
            'cash' : 'Cassa',
            'summa' : '',
            'comment' : '',
            }
        
        widgets = {
            'out_date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'trader': forms.Select(attrs={'class':'form-control', 'placeholder':'Provider'}),
            'cash': forms.Select(attrs={'class':'form-control', 'placeholder':'Cassa'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('date', 'cash', 'summa', 'comment')

        labels = {
            'date': 'YYYY-MM-DD HH:MM:SS',
            'cash' : 'Cassa',
            'summa' : '',
            'comment' : '',
            }
        
        widgets = {
            'date': forms.TextInput(attrs={'type' : 'datetime-local','class':'form-control', 'placeholder':'Sana'}),
            'cash': forms.Select(attrs={'class':'form-control', 'placeholder':'Cassa'}),
            'summa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Summa'}),
            'comment': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Izoh'}),
        }