# Generated by Django 2.0.6 on 2018-09-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blog_blog_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='counter',
        ),
    ]
