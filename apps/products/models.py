from django.db import models
from apps.accounts.models import User
import uuid

# Create your models here.


#Ishlab chiqaruvchilar
class Brand(models.Model):

    name = models.CharField('Brand Nomi', max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', blank=True, max_length=255, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


#Tovarlar
class Product(models.Model):

    name = models.CharField('Tovar Nomi', max_length=50)
    capacity = models.IntegerField('Sigimi', blank=True, null=True,)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete= models.CASCADE)
    product_size = models.FloatField(blank=True, null=True, )
    product_weight = models.FloatField(blank=True, null=True, )
    code = models.IntegerField('Kodi', blank=True, null=True,)
    image = models.ImageField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    price = models.IntegerField('Narxi',  blank=True, null=True,)
    s_price = models.IntegerField('Snarxi',  blank=True, null=True,)

    def __str__(self):
        return self.name


#Omborlar
class WarehouseName(models.Model):

    name = models.CharField('Ombor Nomi', max_length=50)
    warehouse_size = models.FloatField(blank=True, null=True,)

    def __str__(self):
        return self.name

#InDocument
class InDocument(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, blank=True, null=True,)
    in_date = models.DateTimeField('Sana',)
    provider = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="buy_provider", limit_choices_to ={'user_type':'PR'})
    warehouse = models.ForeignKey(WarehouseName, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField('Summa',  blank=True, null=True,default=0)
    comment = models.TextField(blank=True, null=True, default='Tovar kirimi',)

    class Meta:
        ordering = ['-in_date']

    def __str__(self):
        return f'{self.provider} {self.in_date}'


#OutDocument
class OutDocument(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, blank=True, null=True,)
    out_date = models.DateTimeField('Sana',)
    trader = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="buyer", limit_choices_to ={'user_type':'PR'})
    warehouse = models.ForeignKey(WarehouseName, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField('Summa',  blank=True, null=True,default=0)
    profit = models.IntegerField('Foyda', blank=True, null=True,default=0)
    comment = models.TextField(blank=True, null=True, default='Tovar chiqimi',)

    class Meta:
        ordering = ['-out_date']

    def __str__(self):
        return f'{self.trader} {self.out_date}'

#OutDocumentClient
class OutDocumentClient(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, blank=True, null=True,)
    out_date = models.DateTimeField('Sana',)
    trader = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="buyer_seller", limit_choices_to ={'user_type':'PR'})
    client = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="shopkeeper", limit_choices_to ={'user_type':'CL'})
    warehouse = models.ForeignKey(WarehouseName, blank=True, null=True, on_delete= models.CASCADE)
    summa = models.IntegerField('Summa',  blank=True, null=True,default=0)
    ssumma = models.IntegerField('SSumma',  blank=True, null=True,default=0)
    profit = models.IntegerField('Foyda', blank=True, null=True,default=0)
    sprofit = models.IntegerField('Sfoyda', blank=True, null=True,default=0)
    comment = models.TextField(blank=True, null=True, default='Tovar chiqimi B',)

    class Meta:
        ordering = ['-out_date']

    def __str__(self):
        return f'{self.client} {self.out_date}'


#Tovar kirim qilish
class InProduct(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, blank=True, null=True,)
    document = models.ForeignKey(InDocument, blank=True, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.CASCADE)
    quantity = models.IntegerField('Soni', )
    body_price = models.IntegerField('Tannarxi',  )
    body_summa = models.IntegerField('TanSumma',  )
    price = models.IntegerField('Narxi',  )
    summa = models.IntegerField('Summa',  )
    shop_price = models.IntegerField('Snarxi',  )
    shop_summa = models.IntegerField('Ssumma', )

    def __str__(self):
        return self.document.provider.username


#Tovar chiqim qilish
class OutProduct(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, blank=True, null=True,)
    document = models.ForeignKey(OutDocument, blank=True, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.CASCADE)
    quantity = models.IntegerField('Soni',  )
    body_price = models.IntegerField('Tannarxi',  )
    body_summa = models.IntegerField('TanSumma',  )
    price = models.IntegerField('Narxi',  )
    summa = models.IntegerField('Summa',  )
    profit = models.IntegerField('Foyda', )

    def __str__(self):
        return self.document.trader.username


# B Tovar chiqim qilish
class OutProductB(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4,  blank=True, null=True)
    document = models.ForeignKey(OutDocumentClient, blank=True, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.CASCADE)
    quantity = models.IntegerField('Soni',  )
    body_price = models.IntegerField('Tannarxi',  )
    body_summa = models.IntegerField('TanSumma',  )
    price = models.IntegerField('Narxi',  )
    summa = models.IntegerField('Summa',  )
    shop_price = models.IntegerField('Snarxi',  )
    shop_summa = models.IntegerField('Ssumma', )
    profit = models.IntegerField('Foyda', )
    sprofit = models.IntegerField('Sfoyda', )

    def __str__(self):
        return self.document.client.username


#Omborlar 
class Warehouse(models.Model):

    event_id = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField('Sana',blank=True, null=True,)
    warehouse = models.ForeignKey(WarehouseName, blank=True, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.CASCADE)
    quantity = models.IntegerField('Soni', blank=True, null=True,)
    body_price = models.IntegerField('Tannarxi',  blank=True, null=True,)
    body_summa = models.IntegerField('TanSumma',  blank=True, null=True,)
    price = models.IntegerField('Narxi',  blank=True, null=True,)
    summa = models.IntegerField('Summa',  blank=True, null=True,)
    shop_price = models.IntegerField('Snarxi',  blank=True, null=True,)
    shop_summa = models.IntegerField('Ssumma', blank=True, null=True,)
    comment = models.TextField(blank=True, null=True,)

    class Meta:
        ordering = ['product']

    def __str__(self):
        return self.comment