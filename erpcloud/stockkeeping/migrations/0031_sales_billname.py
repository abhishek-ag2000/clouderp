# Generated by Django 2.0.6 on 2018-11-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0030_auto_20181103_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='billname',
            field=models.CharField(default='Customer', max_length=32),
        ),
    ]
