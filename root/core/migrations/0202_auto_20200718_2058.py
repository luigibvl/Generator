# Generated by Django 3.0.7 on 2020-07-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0201_auto_20200718_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(default='2020-07-18 20:58:43'),
        ),
        migrations.AlterField(
            model_name='radiomics_study',
            name='num_patients',
            field=models.CharField(default='-1', max_length=100),
        ),
    ]
