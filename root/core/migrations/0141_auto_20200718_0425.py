# Generated by Django 3.0.7 on 2020-07-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0140_auto_20200718_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-18 04:25:08'),
        ),
    ]
