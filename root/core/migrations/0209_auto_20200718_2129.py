# Generated by Django 3.0.7 on 2020-07-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0208_auto_20200718_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(default='2020-07-18 21:29:53'),
        ),
    ]
