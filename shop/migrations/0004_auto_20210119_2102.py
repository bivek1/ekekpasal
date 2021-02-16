# Generated by Django 3.1.5 on 2021-01-19 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_imagelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='SKU',
        ),
        migrations.RemoveField(
            model_name='product',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tax',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variant',
        ),
        migrations.AddField(
            model_name='product',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_service', to='shop.service'),
            preserve_default=False,
        ),
    ]