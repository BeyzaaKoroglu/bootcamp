# Generated by Django 3.2.9 on 2021-12-05 06:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_categories'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baskets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('submitted', 'Submitted'), ('merged', 'Merged')], default='open', max_length=10, verbose_name='Basket Status'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baskets.basket', verbose_name='Basket'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Product'),
        ),
    ]
