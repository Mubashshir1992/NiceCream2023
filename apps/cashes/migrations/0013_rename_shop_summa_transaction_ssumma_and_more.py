# Generated by Django 4.1.6 on 2023-02-28 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashes', '0012_remove_transaction_cash_ssumma'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='shop_summa',
            new_name='ssumma',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='body_summa',
        ),
    ]
