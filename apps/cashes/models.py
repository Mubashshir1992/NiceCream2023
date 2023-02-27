import uuid
from django.db import models
from apps.accounts.models import User

# Create your models here.

#Kassa nomlari
class Cash(models.Model):

    name = models.CharField('Kassa Nomi', max_length=50)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


#Pul kirimi
class InCash(models.Model):

    in_date = models.DateTimeField('Sana',)
    trader = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="payer", limit_choices_to ={'user_type':'PR'})
    cash = models.ForeignKey(Cash, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Pul kirimi',)

    class Meta:
        ordering = ['-in_date']

    def __str__(self):
        return self.trader.username

#Pul kirimi client
class InCashClient(models.Model):

    in_date = models.DateTimeField('Sana',)
    client = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="client_payer", limit_choices_to ={'user_type':'CL'})
    ssumma = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Pul kirimi client',)

    class Meta:
        ordering = ['-in_date']

    def __str__(self):
        return self.client


#Pul chiqimi
class OutCash(models.Model):

    out_date = models.DateTimeField('Sana',)
    trader = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="payee", limit_choices_to ={'user_type':'PR'})
    cash = models.ForeignKey(Cash, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Pul chiqimi',)

    class Meta:
        ordering = ['-out_date']

    def __str__(self):
        return self.trader

#Xarajat
class Expense(models.Model):
    date = models.DateTimeField('Sana',)
    cash = models.ForeignKey(Cash, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Xarajat',)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.comment}: {self.summa}'


class Transaction(models.Model):
    trans_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    event_id = models.CharField(max_length=20, blank=True, null=True)
    trans_date = models.CharField(max_length=255, blank=True, null=True)
    provider = models.ForeignKey(User, related_name='transactions_as_provider', on_delete=models.PROTECT, blank=True, null=True, limit_choices_to ={'user_type':'PR'})
    client = models.ForeignKey(User, related_name='transactions_as_client', on_delete=models.PROTECT, blank=True, null=True, limit_choices_to ={'user_type':'CL'})
    cash = models.ForeignKey(Cash, related_name='transactions_as_cash', on_delete=models.PROTECT, blank=True, null=True)
    cash_summa = models.DecimalField(default=0.0, max_digits=16, decimal_places=2)
    cash_ssumma = models.DecimalField(default=0.0, max_digits=16, decimal_places=2)
    body_summa = models.DecimalField('TransTanSumma', default=0.0, max_digits=16, decimal_places=2)
    summa = models.DecimalField('TransSumma', default=0.0, max_digits=16, decimal_places=2)
    shop_summa = models.DecimalField('TransSSumma', default=0.0, max_digits=16, decimal_places=2, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    profit = models.DecimalField(default=0.0, max_digits=16, decimal_places=2)
    sprofit = models.DecimalField(default=0.0, max_digits=16, decimal_places=2)

    class Meta:
        ordering = ['-trans_date']

    def __str__(self):
        return f'{self.trans_date} : {self.comment}'

