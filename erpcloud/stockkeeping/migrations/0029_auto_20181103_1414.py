# Generated by Django 2.0.6 on 2018-11-03 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0028_auto_20181103_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_total',
            name='purchases',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasetotal', to='stockkeeping.Purchase'),
        ),
        migrations.AlterField(
            model_name='stock_total_sales',
            name='sales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saletotal', to='stockkeeping.Sales'),
        ),
    ]
