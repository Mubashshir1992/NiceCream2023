# Generated by Django 4.1.6 on 2023-02-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashes', '0004_remove_incash_client_incashclient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incashclient',
            name='cash',
        ),
    ]
