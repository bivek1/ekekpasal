# Generated by Django 3.1.5 on 2021-01-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210120_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, upload_to='shop_picture'),
        ),
    ]
