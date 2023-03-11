from .models import *
from django.db.models.signals import post_save, post_delete
from apps.cashes.models import Transaction
from django.dispatch import receiver


@receiver(post_save, sender=InProduct)
def creat_trans_inProduct(sender, instance, created, **kwargs):
    if created:
        # Transaction.objects.create(
        #     trans_date=instance.document.in_date,
        #     comment = instance.document.comment,
        #     provider = instance.document.provider,
        #     summa = instance.body_summa,
        #     event_id = instance.event_id
        # )

        Warehouse.objects.create(
            date = instance.document.in_date,
            warehouse = instance.document.warehouse,
            product = instance.product,
            quantity = instance.quantity,
            body_price = instance.body_price,
            body_summa = instance.body_summa,
            price = instance.price,
            summa = instance.summa,
            shop_price = instance.shop_price,
            shop_summa = instance.shop_summa,
            comment = instance.document.comment,
            event_id = instance.event_id,
        )

        provider = User.objects.filter(user_type = 'PR').get(username=instance.document.provider)
        provider.balance += instance.body_summa
        provider.save()
        
        qs = InDocument.objects.get(event_id=instance.document.event_id)
        qs.summa += instance.body_summa
        qs.save()

    else:
        # tr = Transaction.objects.get(event_id=instance.event_id)
        # tr.trans_date=instance.document.in_date
        # tr.comment = instance.document.comment
        # tr.provider = instance.document.provider
        # tr.summa = instance.body_summa
        # tr.event_id = instance.event_id
        # tr.save()

        wr = Warehouse.objects.get(event_id=instance.event_id)
        wr.date = instance.document.in_date
        wr.warehouse = instance.document.warehouse
        wr.product = instance.product
        wr.quantity = instance.quantity
        wr.body_price = instance.body_price
        wr.body_summa = instance.body_summa
        wr.price = instance.price
        wr.summa = instance.summa
        wr.shop_price = instance.shop_price
        wr.shop_summa = instance.shop_summa
        wr.comment = instance.document.comment
        wr.event_id = instance.event_id
        wr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.document.provider)
        provider.balance += instance.body_summa
        provider.save()

        qs = InDocument.objects.get(event_id=instance.document.event_id)
        qs.summa += instance.body_summa
        qs.save()


@receiver(post_delete, sender=InProduct)
def delete_trans_inProduct(sender, instance, **kwargs):
    
    provider = User.objects.filter(user_type = 'PR').get(username=instance.document.provider)
    provider.balance -= instance.body_summa
    provider.save()

    qs = InDocument.objects.get(event_id=instance.document.event_id)
    qs.summa -= instance.body_summa
    qs.save()

    # trans = Transaction.objects.get(event_id=instance.event_id)
    # trans.delete()
    wr = Warehouse.objects.get(event_id=instance.event_id)
    wr.delete()

@receiver(post_save, sender=OutProduct)
def creat_trans_outProduct(sender, instance, created, **kwargs):
    if created:
        # Transaction.objects.create(
        #     trans_date=instance.document.out_date,
        #     comment = instance.document.comment,
        #     provider = instance.document.trader,
        #     summa = -instance.summa,
        #     event_id = instance.event_id,
        #     profit = instance.profit
        # )

        Warehouse.objects.create(
            date = instance.document.out_date,
            warehouse = instance.document.warehouse,
            product = instance.product,
            quantity = -instance.quantity,
            body_price = -instance.body_price,
            body_summa = -instance.body_summa,
            price = -instance.price,
            summa = -instance.summa,
            comment = instance.document.comment,
            event_id = instance.event_id,
        )

        provider = User.objects.filter(user_type = 'PR').get(username=instance.document.trader)
        provider.balance -= instance.summa
        provider.save()

        qs = OutDocument.objects.get(event_id=instance.document.event_id)
        qs.summa -= instance.summa
        qs.profit += instance.profit
        qs.save()

    else:
        # tr = Transaction.objects.get(event_id=instance.event_id)
        # tr.trans_date = instance.document.out_date
        # tr.comment = instance.document.comment
        # tr.provider = instance.document.trader
        # tr.summa = -instance.summa
        # tr.event_id = instance.event_id
        # tr.profit = instance.profit
        # tr.save()

        wr = Warehouse.objects.get(event_id=instance.event_id)
        wr.date = instance.document.out_date
        wr.warehouse = instance.document.warehouse
        wr.product = instance.product
        wr.quantity = -instance.quantity
        wr.body_price = -instance.body_price
        wr.body_summa = -instance.body_summa
        wr.price = -instance.price
        wr.summa = -instance.summa
        wr.comment = instance.document.comment
        wr.event_id = instance.event_id
        wr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.document.trader)
        provider.balance -= instance.summa
        provider.save()

        qs = OutDocument.objects.get(event_id=instance.document.event_id)
        qs.summa -= instance.summa
        qs.profit += instance.profit
        qs.save()
      

@receiver(post_delete, sender=OutProduct)
def delete_trans_outProduct(sender, instance, **kwargs):

    provider = User.objects.filter(user_type = 'PR').get(username=instance.document.trader)
    provider.balance += instance.summa
    provider.save()

    qs = OutDocument.objects.get(event_id=instance.document.event_id)
    qs.summa += instance.summa
    qs.profit -= instance.profit
    qs.save()

    # trans = Transaction.objects.get(event_id=instance.event_id)
    # trans.delete()
    wr = Warehouse.objects.get(event_id=instance.event_id)
    wr.delete()

@receiver(post_save, sender=OutProductB)
def creat_trans_outProductB(sender, instance, created, **kwargs):
    if created:
        # Transaction.objects.create(
        #     trans_date=instance.document.out_date,
        #     comment = instance.document.comment,
        #     provider = instance.document.trader,
        #     client = instance.document.client,
        #     summa = -instance.summa,
        #     ssumma = -instance.shop_summa,
        #     event_id = instance.event_id,
        #     profit = instance.profit,
        #     sprofit = instance.sprofit
        # )

        Warehouse.objects.create(
            date = instance.document.out_date,
            warehouse = instance.document.warehouse,
            product = instance.product,
            quantity = -instance.quantity,
            body_price = -instance.body_price,
            body_summa = -instance.body_summa,
            price = -instance.price,
            summa = -instance.summa,
            shop_price = -instance.shop_price,
            shop_summa = -instance.shop_summa,
            comment = instance.document.comment,
            event_id = instance.event_id,
        )

        provider = User.objects.filter(user_type = 'PR').get(username=instance.document.trader)
        provider.balance -= instance.summa
        provider.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.document.client)
        client.balance -= instance.shop_summa
        client.save()

        qs = OutDocumentClient.objects.get(event_id=instance.document.event_id)
        qs.summa -= instance.summa
        qs.ssumma -= instance.shop_summa
        qs.profit += instance.profit
        qs.sprofit += instance.sprofit
        qs.save()

    else:
        # tr = Transaction.objects.get(event_id=instance.event_id)
        # tr.trans_date=instance.document.out_date
        # tr.comment = instance.document.comment
        # tr.provider = instance.document.trader
        # tr.client = instance.document.client
        # tr.summa = -instance.summa
        # tr.ssumma = -instance.shop_summa
        # tr.event_id = instance.event_id
        # tr.profit = instance.profit
        # tr.sprofit = instance.sprofit
        # tr.save()

        wr = Warehouse.objects.get(event_id=instance.event_id)
        wr.date = instance.document.out_date
        wr.warehouse = instance.document.warehouse
        wr.product = instance.product
        wr.quantity = -instance.quantity
        wr.body_price = -instance.body_price
        wr.body_summa = -instance.body_summa
        wr.price = -instance.price
        wr.summa = -instance.summa
        wr.shop_price = -instance.shop_price
        wr.shop_summa = -instance.shop_summa
        wr.comment = instance.document.comment
        wr.event_id = instance.event_id
        wr.save()

        provider = User.objects.filter(user_type = 'PR').get(username=instance.document.trader)
        provider.balance -= instance.summa
        provider.save()

        client = User.objects.filter(user_type = 'CL').get(username=instance.document.client)
        client.balance -= instance.shop_summa
        client.save()

        qs = OutDocumentClient.objects.get(event_id=instance.document.event_id)
        qs.summa -= instance.summa
        qs.ssumma -= instance.shop_summa
        qs.profit += instance.profit
        qs.sprofit += instance.sprofit
        qs.save()
      

@receiver(post_delete, sender=OutProductB)
def delete_trans_outProductB(sender, instance, **kwargs):
    
    provider = User.objects.filter(user_type = 'PR').get(username=instance.document.trader)
    provider.balance += instance.summa
    provider.save()

    client = User.objects.filter(user_type = 'CL').get(username=instance.document.client)
    client.balance += instance.shop_summa
    client.save()

    qs = OutDocumentClient.objects.get(event_id=instance.document.event_id)
    qs.summa += instance.summa
    qs.ssumma += instance.shop_summa
    qs.profit -= instance.profit
    qs.sprofit -= instance.sprofit
    qs.save()

    # trans = Transaction.objects.get(event_id=instance.event_id)
    # trans.delete()
    wr = Warehouse.objects.get(event_id=instance.event_id)
    wr.delete()

@receiver(post_save, sender=InDocument)
def creat_trans_inDocument(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.in_date,
            comment = instance.comment,
            provider = instance.provider,
            summa = instance.summa,
            event_id = instance.event_id
        )

    else:
        tr = Transaction.objects.get(event_id=instance.event_id)
        tr.trans_date=instance.in_date
        tr.comment = instance.comment
        tr.provider = instance.provider
        tr.summa = instance.summa
        tr.event_id = instance.event_id
        tr.save()


@receiver(post_delete, sender=InDocument)
def delete_trans_inDocument(sender, instance, **kwargs):
    
    trans = Transaction.objects.get(event_id=instance.event_id)
    trans.delete()


@receiver(post_save, sender=OutDocument)
def creat_trans_outDocument(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            summa = instance.summa,
            profit = instance.profit,
            event_id = instance.event_id,
        )

    else:
        tr = Transaction.objects.get(event_id=instance.event_id)
        tr.trans_date=instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.summa = instance.summa
        tr.profit = instance.profit
        tr.event_id = instance.event_id
        tr.save()


@receiver(post_delete, sender=OutDocument)
def delete_trans_outDocument(sender, instance, **kwargs):
    
    trans = Transaction.objects.get(event_id=instance.event_id)
    trans.delete()
       

@receiver(post_save, sender=OutDocumentClient)
def creat_trans_outDocumentClient(sender, instance, created, **kwargs):
    if created:
        Transaction.objects.create(
            trans_date=instance.out_date,
            comment = instance.comment,
            provider = instance.trader,
            client = instance.client,
            summa = instance.summa,
            ssumma = instance.ssumma,
            profit = instance.profit,
            sprofit = instance.sprofit,
            event_id = instance.event_id
        )

    else:
        tr = Transaction.objects.get(event_id=instance.event_id)
        tr.trans_date=instance.out_date
        tr.comment = instance.comment
        tr.provider = instance.trader
        tr.client = instance.client
        tr.summa = instance.summa
        tr.ssumma = instance.ssumma
        tr.profit = instance.profit
        tr.sprofit = instance.sprofit
        tr.event_id = instance.event_id
        tr.save()


@receiver(post_delete, sender=OutDocumentClient)
def delete_trans_outDocumentClient(sender, instance, **kwargs):
    
    trans = Transaction.objects.get(event_id=instance.event_id)
    trans.delete()
       