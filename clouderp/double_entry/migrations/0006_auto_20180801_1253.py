# Generated by Django 2.0.7 on 2018-08-01 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('double_entry', '0005_auto_20180801_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='group1',
            name='Group_behaves_like_a_Sub_Ledger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group1',
            name='Nett_Debit_or_Credit_Balances_for_Reporting',
            field=models.BooleanField(default=False),
        ),
    ]
