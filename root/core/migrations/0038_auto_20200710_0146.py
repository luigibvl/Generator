# Generated by Django 3.0.8 on 2020-07-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20200710_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-10 01:46:48'),
        ),
    ]
