# Generated by Django 2.0.5 on 2018-08-22 13:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0008_remove_journal_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('Opening_Balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('User_Name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('State', models.CharField(choices=[('Choose', 'Choose'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisghar', 'Chhattisghar'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharasthra', 'Maharasthra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telengana', 'Telengana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Choose', max_length=100)),
                ('Pin_Code', models.BigIntegerField()),
                ('PanIt_No', models.CharField(blank=True, max_length=100)),
                ('GST_No', models.CharField(blank=True, max_length=100)),
                ('Particulars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_double_entry.transaction')),
                ('Particulars_Credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Creditledgers', to='accounting_double_entry.transaction')),
                ('group1_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_double_entry.group1')),
            ],
        ),
        migrations.RemoveField(
            model_name='journal',
            name='Particulars',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='Particulars_Credit',
        ),
        migrations.RemoveField(
            model_name='ledger1',
            name='group1_Name',
        ),
        migrations.DeleteModel(
            name='journal',
        ),
        migrations.DeleteModel(
            name='ledger1',
        ),
    ]