# Generated by Django 2.0.6 on 2018-10-29 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0002_auto_20181029_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockgroup',
            name='under',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stock_group', to='stockkeeping.Stockgroup'),
        ),
    ]
