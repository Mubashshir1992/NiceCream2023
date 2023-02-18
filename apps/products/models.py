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
    provider = models.ForeignKey(User, blank=True, null=True, on_delete= models.CASCADE, related_name="buy_provider")
    warehouse = models.ForeignKey(Warehouse, blank=True, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.CASCADE)
    quantity = models.IntegerField('Soni', blank=False, )
    body_price = models.IntegerField('Tannarxi', blank=False, )
    body_summa = models.IntegerField('TanSumma', blank=False, )
    price = models.IntegerField('Narxi', blank=False, )
    summa = models.IntegerField('Summa', blank=False, )
    shop_price = models.IntegerField('Snarxi', blank=False, )
    shop_summa = models.IntegerField('Ssumma', blank=False,)
    comment = models.TextField(blank=True, default='Tovar kirimi',)

    def __str__(self):
        return self.provider.username