# Generated by Django 4.1.6 on 2023-02-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='/default/user4.png', upload_to=''),
        ),
    ]
