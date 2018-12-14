# Generated by Django 2.0.6 on 2018-11-02 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0033_auto_20181102_1710'),
        ('stockkeeping', '0023_stock_total_sales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='purchase',
        ),
        migrations.AddField(
            model_name='sales',
            name='sales',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='salesledger', to='accounting_double_entry.ledger1'),
            preserve_default=False,
        ),
    ]
