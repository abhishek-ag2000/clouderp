# Generated by Django 2.0.6 on 2018-12-12 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0040_auto_20181212_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group1',
            name='Master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subgroups', to='accounting_double_entry.group1'),
        ),
    ]
