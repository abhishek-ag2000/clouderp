# Generated by Django 2.0.5 on 2018-08-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0013_auto_20180825_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group1',
            name='group_Name',
            field=models.CharField(error_messages={'unique': 'This Group Name has already been registered'}, max_length=32, unique=True),
        ),
    ]
