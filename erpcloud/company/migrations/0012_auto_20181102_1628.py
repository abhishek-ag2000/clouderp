# Generated by Django 2.0.6 on 2018-11-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_auto_20181029_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='gst',
            field=models.CharField(default='20CEFG6003H1ZZ', max_length=20),
        ),
        migrations.AddField(
            model_name='company',
            name='pan',
            field=models.CharField(default='20CEFG6003H', max_length=18),
        ),
    ]
