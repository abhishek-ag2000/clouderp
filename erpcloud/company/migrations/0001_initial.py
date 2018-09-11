# Generated by Django 2.0.5 on 2018-09-07 10:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Type_of_company', models.CharField(choices=[('Individual', 'Individual'), ('HUF', 'HUF'), ('Partnership', 'Partnership'), ('Trust', 'Trust'), ('Private Company', 'Private Company'), ('Public Company', 'Public Company'), ('LLP', 'LLP')], default='Individual', max_length=32)),
                ('Shared_Users', models.CharField(default='Current User only', max_length=32)),
                ('Address', models.TextField()),
                ('Country', models.CharField(default='India', max_length=32)),
                ('State', models.CharField(choices=[('Choose', 'Choose'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisghar', 'Chhattisghar'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharasthra', 'Maharasthra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telengana', 'Telengana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Choose', max_length=100)),
                ('Pincode', models.CharField(max_length=32)),
                ('Telephone_No', models.BigIntegerField(blank=True, null=True)),
                ('Mobile_No', models.BigIntegerField()),
                ('Financial_Year_From', models.DateTimeField(default=datetime.datetime.now)),
                ('Books_Begining_From', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.CreateModel(
            name='companyowner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company_Name', to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company_Owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='companyowner',
            unique_together={('Company', 'user')},
        ),
    ]
