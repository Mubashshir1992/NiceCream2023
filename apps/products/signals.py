from .models import *
from django.db.models.signals import post_save, post_delete
from apps.cashes.models import Transaction
from django.dispatch import receiver


@receiver(post_save, sender=InProduct)
def creat_trans_inProduct(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.in_date,
            comment = instance.comment,
            provider = instance.provider,
            body_summa = instance.body_summa,
            event_id = instance.id
        )
        provider = User.objects.filter(user_type = 'PR').get(username=instance.provider)
        provider.balance += instance.body_summa
        provider.save()

    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.in_date
        tr.comment = instance.comment
        tr.provider = instance.provider
        tr.body_summa = instance.body_summa
        tr.event_id = instance.id
        tr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.provider)
        provider.balance += instance.body_summa
        provider.save()


@receiver(post_delete, sender=InProduct)
def delete_trans_inProduct(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()

@receiver(post_save, sender=OutProduct)
def creat_trans_outProduct(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            summa = instance.summa,
            event_id = instance.id,
            profit = instance.profit
        )
        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()

    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.summa = instance.summa
        tr.event_id = instance.id
        tr.profit = instance.profit
        tr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()
      

@receiver(post_delete, sender=OutProduct)
def delete_trans_outProduct(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()

@receiver(post_save, sender=OutProductB)
def creat_trans_outProductB(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            client = instance.client,
            summa = instance.summa,
            shop_summa = instance.shop_summa,
            event_id = instance.id,
            profit = instance.profit,
            sprofit = instance.sprofit
        )
        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.client)
        client.balance -= instance.shop_summa
        client.save()

    else:
        tr = Transaction.objects.get(event_id=instance.id)
        tr.trans_date=instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.client = instance.client
        tr.summa = instance.summa
        tr.shop_summa = instance.shop_summa
        tr.event_id = instance.id
        tr.profit = instance.profit
        tr.sprofit = instance.sprofit
        tr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.client)
        client.balance -= instance.shop_summa
        client.save()
      

@receiver(post_delete, sender=OutProductB)
def delete_trans_outProductB(sender, instance, **kwargs):
    trans = Transaction.objects.get(event_id=instance.id)
    trans.delete()