# Generated by Django 2.0.6 on 2018-10-10 08:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20181006_1924'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounting_double_entry', '0017_auto_20181010_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='selectdatefield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateField(blank=True, null=True)),
                ('End_Date', models.DateField(blank=True, null=True)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CompanyDate', to='company.company')),
            ],
        ),
        migrations.RemoveField(
            model_name='journal',
            name='End_Date',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='Start_Date',
        ),
        migrations.AlterField(
            model_name='ledger1',
            name='Creation_Date',
            field=models.DateField(default=datetime.datetime(2018, 10, 10, 14, 20, 53, 555949)),
        ),
        migrations.AddField(
            model_name='selectdatefield',
            name='Journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='journals', to='accounting_double_entry.journal'),
        ),
        migrations.AddField(
            model_name='selectdatefield',
            name='Ledger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ledgers', to='accounting_double_entry.ledger1'),
        ),
        migrations.AddField(
            model_name='selectdatefield',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to=settings.AUTH_USER_MODEL),
        ),
    ]
