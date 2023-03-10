# Generated by Django 4.1.6 on 2023-02-28 19:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_warehouse_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='outproduct',
            name='event_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='outproductb',
            name='event_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
        migrations.AlterField(
            model_name='inproduct',
            name='event_id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='event_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
