# Generated by Django 2.0.6 on 2018-11-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0017_auto_20181102_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_total',
            name='gst_rate',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=4),
        ),
    ]
