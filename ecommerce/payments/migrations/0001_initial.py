# Generated by Django 3.2.9 on 2021-12-03 21:04

import django.db.models.deletion
from django.db import migrations, models

import payments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100, verbose_name='Bank Name')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=100, verbose_name='Bank Account Name')),
                ('iban', models.CharField(max_length=100, validators=[payments.models.IBANValidator()], verbose_name='IBAN')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.bank', verbose_name='Bank Name')),
            ],
            options={
                'verbose_name': 'Bank Account',
                'verbose_name_plural': 'Bank Accounts',
            },
        ),
    ]
