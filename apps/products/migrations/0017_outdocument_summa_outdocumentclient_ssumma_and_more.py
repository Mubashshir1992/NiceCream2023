# Generated by Django 4.1.6 on 2023-03-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_indocument_summa'),
    ]

    operations = [
        migrations.AddField(
            model_name='outdocument',
            name='summa',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Summa'),
        ),
        migrations.AddField(
            model_name='outdocumentclient',
            name='ssumma',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='SSumma'),
        ),
        migrations.AddField(
            model_name='outdocumentclient',
            name='summa',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Summa'),
        ),
    ]
