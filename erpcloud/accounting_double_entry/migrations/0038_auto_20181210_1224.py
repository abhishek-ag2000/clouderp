# Generated by Django 2.0.6 on 2018-12-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0037_ledger1_balance_opening'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger1',
            name='group1_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledgergroups', to='accounting_double_entry.group1'),
        ),
    ]
