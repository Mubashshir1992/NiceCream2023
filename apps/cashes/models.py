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

    def __str__(self):
        return self.trader

#Pul kirimi client
class InCashClient(models.Model):

    in_date = models.DateTimeField('Sana',)
    client = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="client_payer", limit_choices_to ={'user_type':'CL'})
    summa = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Pul kirimi client',)

    def __str__(self):
        return self.client


#Pul chiqimi
class OutCash(models.Model):

    out_date = models.DateTimeField('Sana',)
    trader = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="payee", limit_choices_to ={'user_type':'PR'})
    cash = models.ForeignKey(Cash, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Pul chiqimi',)

    def __str__(self):
        return self.trader

#Xarajat
class Expense(models.Model):
    date = models.DateTimeField('Sana',)
    cash = models.ForeignKey(Cash, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField(null=True,)
    comment = models.TextField(blank=True, null=True, default='Xarajat',)

    def __str__(self):
        return f'{self.comment}: {self.summa}'