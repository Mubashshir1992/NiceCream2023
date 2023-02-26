from django.contrib import admin
from .models import Cash, InCash, InCashClient, Expense, Transaction

# Register your models here.
admin.site.register(Cash)
admin.site.register(InCash)
admin.site.register(InCashClient)
admin.site.register(Expense)
admin.site.register(Transaction)