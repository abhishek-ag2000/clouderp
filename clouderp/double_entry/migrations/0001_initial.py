# Generated by Django 2.0.7 on 2018-07-31 12:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Master', models.CharField(choices=[('Primary', 'Primary'), ('Fixed_Asset', 'Fixed_Asset'), ('Current_Assets', 'Current_Assets'), ('Liabilities', 'Liabilities'), ('Current_Liabilities', 'Current_Liabilities'), ('Capital', 'Capital'), ('Loans', 'Loans'), ('Income', 'Income'), ('Expenses', 'Expenses')], default='Primary', max_length=32)),
                ('balance_nature', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit'), ('Not Applicable', 'Not Applicable')], default='Debit', max_length=32)),
                ('Nature_of_Group', models.CharField(choices=[('Assets', 'Assets'), ('Expenses', 'Expenses'), ('Income', 'Income'), ('Liabilities', 'Liabilities'), ('Not Applicable', 'Not Applicable')], default='Assets', max_length=32)),
                ('Group_Name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('Opening_Balance', models.FloatField(default=0.0)),
                ('Closing_Balance', models.FloatField(blank=True, default=0.0)),
                ('Group_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='double_entry.group')),
            ],
        ),
    ]
