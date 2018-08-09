# Generated by Django 2.0.7 on 2018-07-18 10:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('Account_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Account_Name', models.CharField(max_length=256)),
                ('Account_Type', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address_Line_1', models.CharField(max_length=256)),
                ('Address_Line_2', models.CharField(max_length=256)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=40)),
                ('Phone_No', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Master', models.CharField(choices=[('Fixed_Asset', 'Fixed_Asset'), ('Current_Assets', 'Current_Assets'), ('Liabilities', 'Liabilities'), ('Current_Liabilities', 'Current_Liabilities'), ('Capital', 'Capital'), ('Loans', 'Loans'), ('Income', 'Income'), ('Expenses', 'Expenses')], default='Fixed_Asset', max_length=32)),
                ('balance_nature', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit'), ('Not Applicable', 'Not Applicable')], default='Debit', max_length=32)),
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
                ('Group_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Double_entryy.group')),
            ],
        ),
        migrations.CreateModel(
            name='line_Item',
            fields=[
                ('line_ItemID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.PositiveIntegerField()),
                ('Memo_2', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('Transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Memo_1', models.CharField(max_length=256)),
                ('ref', models.CharField(blank=True, max_length=256)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Double_entryy.contact')),
            ],
        ),
        migrations.AddField(
            model_name='line_item',
            name='Transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Double_entryy.transaction'),
        ),
        migrations.AddField(
            model_name='account',
            name='line_ItemID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Double_entryy.line_Item'),
        ),
    ]
