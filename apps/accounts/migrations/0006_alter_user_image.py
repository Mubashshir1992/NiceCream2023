# Generated by Django 4.1.6 on 2023-02-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='user4.png', null=True, upload_to='images/'),
        ),
    ]
