# Generated by Django 2.0.6 on 2018-10-25 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0026_auto_20181013_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger1',
            name='Closing_balance',
        ),
    ]
