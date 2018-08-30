# Generated by Django 2.0.5 on 2018-08-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0020_auto_20180828_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger1',
            name='Total_Credit',
        ),
        migrations.RemoveField(
            model_name='ledger1',
            name='Total_Debit',
        ),
        migrations.AlterField(
            model_name='ledger1',
            name='Closing_Balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
