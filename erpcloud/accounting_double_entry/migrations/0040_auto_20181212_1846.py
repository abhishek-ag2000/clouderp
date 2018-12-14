# Generated by Django 2.0.6 on 2018-12-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0039_auto_20181212_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group1',
            name='Master',
            field=models.CharField(choices=[('Primary', 'Primary'), ('Fixed_Asset', 'Fixed_Asset'), ('Current_Assets', 'Current_Assets'), ('Liabilities', 'Liabilities'), ('Current_Liabilities', 'Current_Liabilities'), ('Capital', 'Capital'), ('Loans', 'Loans'), ('Income', 'Income'), ('Expenses', 'Expenses')], default='Primary', max_length=32),
        ),
    ]