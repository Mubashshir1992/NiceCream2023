from .models import *
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=InCash)
def creat_trans_inCash(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.in_date,
            comment = instance.comment,
            provider = instance.trader,
            cash = instance.cash,
            cash_summa = instance.summa,
            event_id = instance.id
        )
        trader = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        trader.balance += instance.summa
        trader.save()

        cash = Cash.objects.get(name=instance.cash)
        cash.balance += instance.summa
        cash.save()
    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.in_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.cash = instance.cash
        tr.cash_summa = instance.summa
        tr.event_id = instance.id
        tr.save()

        trader = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        trader.balance += instance.summa
        trader.save()

        cash = Cash.objects.get(name=instance.cash)
        cash.balance += instance.summa
        cash.save()


@receiver(post_delete, sender=InCash)
def delete_trans_inCash(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()

@receiver(post_save, sender=InCashClient)
def creat_trans_inCash(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.in_date,
            comment = instance.comment,
            client = instance.client,
            cash_ssumma = instance.ssumma,
            event_id = instance.id
        )
        client = User.objects.filter(user_type = 'CL').get(username=instance.client)
        client.balance += instance.ssumma
        client.save()

    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.in_date
        tr.comment = instance.comment
        tr.client = instance.client
        tr.cash_ssumma = instance.ssumma
        tr.event_id = instance.id
        tr.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.client)
        client.balance += instance.ssumma
        client.save()
      

@receiver(post_delete, sender=InCashClient)
def delete_trans_inCashClient(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()


@receiver(post_save, sender=OutCash)
def creat_trans_inCash(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            cash = instance.cash,
            cash_summa = instance.summa,
            event_id = instance.id
        )
        trader = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        trader.balance -= instance.summa
        trader.save()

        cash = Cash.objects.get(name=instance.cash)
        cash.balance -= instance.summa
        cash.save()
    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.cash = instance.cash
        tr.cash_summa = instance.summa
        tr.event_id = instance.id
        tr.save()

        trader = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        trader.balance -= instance.summa
        trader.save()

        cash = Cash.objects.get(name=instance.cash)
        cash.balance -= instance.summa
        cash.save()


@receiver(post_delete, sender=OutCash)
def delete_trans_inCash(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()


@receiver(post_save, sender=Expense)
def creat_trans_expense(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.date,
            comment = instance.comment,
            cash = instance.cash,
            cash_summa = instance.summa,
            event_id = instance.id
        )

        cash = Cash.objects.get(name=instance.cash)
        cash.balance -= instance.summa
        cash.save()

    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.date
        tr.comment = instance.comment
        tr.cash = instance.cash
        tr.cash_summa = instance.summa
        tr.event_id = instance.id
        tr.save()

        cash = Cash.objects.get(name=instance.cash)
        cash.balance -= instance.summa
        cash.save()


@receiver(post_delete, sender=Expense)
def delete_trans_expense(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()