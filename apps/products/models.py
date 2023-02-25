from django.db import models
from apps.accounts.models import User

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

    def __str__(self):
        return self.name


#Omborlar
class Warehouse(models.Model):

    name = models.CharField('Ombor Nomi', max_length=50)
    warehouse_size = models.FloatField(blank=True, null=True,)

    def __str__(self):
        return self.name


#Tovar kirim qilish
class InProduct(models.Model):

    in_date = models.DateTimeField('Sana',)
    provider = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="buy_provider", limit_choices_to ={'user_type':'PR'})
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.CASCADE)
    quantity = models.IntegerField('Soni', )
    body_price = models.IntegerField('Tannarxi',  )
    body_summa = models.IntegerField('TanSumma',  )
    price = models.IntegerField('Narxi',  )
    summa = models.IntegerField('Summa',  )
    shop_price = models.IntegerField('Snarxi',  )
    shop_summa = models.IntegerField('Ssumma', )
    comment = models.TextField(blank=True, null=True, default='Tovar kirimi',)

    def __str__(self):
        return self.provider.username


#Tovar chiqim qilish
class OutProduct(models.Model):

    out_date = models.DateTimeField('Sana',)
    trader = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="buyer_seller", limit_choices_to ={'user_type':'PR'})
    client = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="shopkeeper", limit_choices_to ={'user_type':'CL'})
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete= models.CASCADE)
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
    comment = models.TextField(blank=True, null=True, default='Tovar chiqimi',)

    def __str__(self):
        return self.trader.username