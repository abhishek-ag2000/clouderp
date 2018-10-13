# Generated by Django 2.0.6 on 2018-10-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0008_auto_20181002_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger1',
            name='Closing_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ledger1',
            name='Pin_Code',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
