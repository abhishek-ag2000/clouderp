# Generated by Django 2.0.6 on 2018-10-29 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockgroup',
            name='under',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Stock_group', to='stockkeeping.Stockgroup'),
        ),
    ]
