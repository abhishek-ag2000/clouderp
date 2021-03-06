# Generated by Django 2.0.6 on 2018-12-14 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0047_auto_20181214_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='group',
            name='User',
        ),
        migrations.RemoveField(
            model_name='group1',
            name='Total_closing_balance',
        ),
        migrations.RemoveField(
            model_name='group1',
            name='Total_opening_balance',
        ),
        migrations.AddField(
            model_name='group1',
            name='Nature_of_group1',
            field=models.CharField(choices=[('Assets', 'Assets'), ('Expenses', 'Expenses'), ('Income', 'Income'), ('Liabilities', 'Liabilities'), ('Not Applicable', 'Not Applicable')], default='Assets', max_length=32),
        ),
        migrations.AlterField(
            model_name='group1',
            name='Master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_group', to='accounting_double_entry.group1'),
        ),
        migrations.DeleteModel(
            name='group',
        ),
    ]
