# Generated by Django 4.1.6 on 2023-02-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_warehousename_alter_warehouse_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]