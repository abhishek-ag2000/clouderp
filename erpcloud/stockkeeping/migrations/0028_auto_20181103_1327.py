# Generated by Django 2.0.6 on 2018-11-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0027_auto_20181103_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='Contact',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Contact',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]