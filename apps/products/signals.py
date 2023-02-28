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
            summa = instance.body_summa,
            event_id = instance.event_id
        )

        Warehouse.objects.create(
            date = instance.in_date,
            warehouse = instance.warehouse,
            product = instance.product,
            quantity = instance.quantity,
            body_price = instance.body_price,
            body_summa = instance.body_summa,
            price = instance.price,
            summa = instance.summa,
            shop_price = instance.shop_price,
            shop_summa = instance.shop_summa,
            comment = instance.comment,
            event_id = instance.event_id,
        )

        provider = User.objects.filter(user_type = 'PR').get(username=instance.provider)
        provider.balance += instance.body_summa
        provider.save()

    else:
        tr = Transaction.objects.get(event_id=instance.event_id)
        tr.trans_date=instance.in_date
        tr.comment = instance.comment
        tr.provider = instance.provider
        tr.summa = instance.body_summa
        tr.event_id = instance.event_id
        tr.save()

        wr = Warehouse.objects.get(event_id=instance.event_id)
        wr.date = instance.in_date
        wr.warehouse = instance.warehouse
        wr.product = instance.product
        wr.quantity = instance.quantity
        wr.body_price = instance.body_price
        wr.body_summa = instance.body_summa
        wr.price = instance.price
        wr.summa = instance.summa
        wr.shop_price = instance.shop_price
        wr.shop_summa = instance.shop_summa
        wr.comment = instance.comment
        wr.event_id = instance.event_id
        wr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.provider)
        provider.balance += instance.body_summa
        provider.save()


@receiver(post_delete, sender=InProduct)
def delete_trans_inProduct(sender, instance, **kwargs):
    
    provider = User.objects.filter(user_type = 'PR').get(username=instance.provider)
    provider.balance -= instance.body_summa
    provider.save()

    trans = Transaction.objects.get(event_id=instance.event_id)
    trans.delete()
    wr = Warehouse.objects.get(event_id=instance.event_id)
    wr.delete()

@receiver(post_save, sender=OutProduct)
def creat_trans_outProduct(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            summa = -instance.summa,
            event_id = instance.event_id,
            profit = instance.profit
        )

        Warehouse.objects.create(
            date = instance.out_date,
            warehouse = instance.warehouse,
            product = instance.product,
            quantity = -instance.quantity,
            body_price = -instance.body_price,
            body_summa = -instance.body_summa,
            price = -instance.price,
            summa = -instance.summa,
            comment = instance.comment,
            event_id = instance.event_id,
        )

        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()

    else:
        tr = Transaction.objects.get(event_id=instance.event_id)
        tr.trans_date = instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.summa = -instance.summa
        tr.event_id = instance.event_id
        tr.profit = instance.profit
        tr.save()

        wr = Warehouse.objects.get(event_id=instance.event_id)
        wr.date = instance.out_date
        wr.warehouse = instance.warehouse
        wr.product = instance.product
        wr.quantity = -instance.quantity
        wr.body_price = -instance.body_price
        wr.body_summa = -instance.body_summa
        wr.price = -instance.price
        wr.summa = -instance.summa
        wr.comment = instance.comment
        wr.event_id = instance.event_id
        wr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()
      

@receiver(post_delete, sender=OutProduct)
def delete_trans_outProduct(sender, instance, **kwargs):

    provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
    provider.balance += instance.summa
    provider.save()

    trans = Transaction.objects.get(event_id=instance.event_id)
    trans.delete()
    wr = Warehouse.objects.get(event_id=instance.event_id)
    wr.delete()

@receiver(post_save, sender=OutProductB)
def creat_trans_outProductB(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            client = instance.client,
            summa = -instance.summa,
            ssumma = -instance.shop_summa,
            event_id = instance.event_id,
            profit = instance.profit,
            sprofit = instance.sprofit
        )

        Warehouse.objects.create(
            date = instance.out_date,
            warehouse = instance.warehouse,
            product = instance.product,
            quantity = -instance.quantity,
            body_price = -instance.body_price,
            body_summa = -instance.body_summa,
            price = -instance.price,
            summa = -instance.summa,
            shop_price = -instance.shop_price,
            shop_summa = -instance.shop_summa,
            comment = instance.comment,
            event_id = instance.event_id,
        )

        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.client)
        client.balance -= instance.shop_summa
        client.save()

    else:
        tr = Transaction.objects.get(event_id=instance.event_id)
        tr.trans_date=instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.client = instance.client
        tr.summa = -instance.summa
        tr.ssumma = -instance.shop_summa
        tr.event_id = instance.event_id
        tr.profit = instance.profit
        tr.sprofit = instance.sprofit
        tr.save()

        wr = Warehouse.objects.get(event_id=instance.event_id)
        wr.date = instance.out_date
        wr.warehouse = instance.warehouse
        wr.product = instance.product
        wr.quantity = -instance.quantity
        wr.body_price = -instance.body_price
        wr.body_summa = -instance.body_summa
        wr.price = -instance.price
        wr.summa = -instance.summa
        wr.shop_price = -instance.shop_price
        wr.shop_summa = -instance.shop_summa
        wr.comment = instance.comment
        wr.event_id = instance.event_id
        wr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
        provider.balance -= instance.summa
        provider.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.client)
        client.balance -= instance.shop_summa
        client.save()
      

@receiver(post_delete, sender=OutProductB)
def delete_trans_outProductB(sender, instance, **kwargs):
    
    provider = User.objects.filter(user_type = 'PR').get(username=instance.trader)
    provider.balance += instance.summa
    provider.save()

    client = User.objects.filter(user_type = 'CL').get(username=instance.client)
    client.balance += instance.shop_summa
    client.save()

    trans = Transaction.objects.get(event_id=instance.event_id)
    trans.delete()
    wr = Warehouse.objects.get(event_id=instance.event_id)
    wr.delete()