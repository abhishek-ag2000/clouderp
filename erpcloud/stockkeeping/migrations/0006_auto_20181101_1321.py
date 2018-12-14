# Generated by Django 2.0.6 on 2018-11-01 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_auto_20181029_1803'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockkeeping', '0005_auto_20181029_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='Amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase_total',
            name='purchases',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasetotal', to='stockkeeping.Purchase'),
        ),
    ]