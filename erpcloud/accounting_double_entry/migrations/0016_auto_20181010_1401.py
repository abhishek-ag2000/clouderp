# Generated by Django 2.0.6 on 2018-10-10 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0015_auto_20181010_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger1',
            name='Creation_Date',
            field=models.DateField(default=datetime.datetime(2018, 10, 10, 14, 1, 31, 201466)),
        ),
    ]
