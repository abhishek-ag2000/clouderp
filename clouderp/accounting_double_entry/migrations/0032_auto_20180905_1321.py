# Generated by Django 2.0.5 on 2018-09-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0031_auto_20180905_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='Total_Debit',
        ),
        migrations.AddField(
            model_name='ledger1',
            name='Total_Debit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
