# Generated by Django 2.0.7 on 2018-08-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='Group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounting_double_entry.group1'),
        ),
    ]
