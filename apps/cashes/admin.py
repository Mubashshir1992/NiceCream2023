from django.contrib import admin
from .models import Cash, InCash, InCashClient, Expense, Transaction, OutCash

class InCashAdmin(admin.ModelAdmin):
    model = InCash
    list_display = ['cash', 'in_date', 'trader', 'summa', 'comment',]

class InCashClientAdmin(admin.ModelAdmin):
    model = InCashClient
    list_display = [ 'in_date', 'client', 'ssumma', 'comment',]

class OutCashAdmin(admin.ModelAdmin):
    model = OutCash
    list_display = ['cash', 'out_date', 'trader', 'summa', 'comment',]

class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = ['cash', 'date', 'summa', 'comment',]   

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ['cash', 'trans_date', 'provider', 'summa', 'client', 'comment',] 

# Register your models here.
admin.site.register(Cash)
admin.site.register(InCash, InCashAdmin)
admin.site.register(OutCash, OutCashAdmin)
admin.site.register(InCashClient, InCashClientAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Transaction, TransactionAdmin)