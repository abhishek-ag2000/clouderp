# Generated by Django 2.0.6 on 2018-12-13 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0041_auto_20181212_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group1',
            name='Master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subgroups', to='accounting_double_entry.group1'),
        ),
    ]
