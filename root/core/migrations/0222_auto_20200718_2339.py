# Generated by Django 3.0.7 on 2020-07-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0221_auto_20200718_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(default='2020-07-18 23:39:05'),
        ),
    ]
