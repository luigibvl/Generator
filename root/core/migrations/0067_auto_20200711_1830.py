# Generated by Django 3.0.8 on 2020-07-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20200711_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-11 18:30:06'),
        ),
    ]
