# Generated by Django 2.0.6 on 2018-09-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180920_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='Categorycount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
