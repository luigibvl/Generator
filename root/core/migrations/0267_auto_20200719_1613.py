# Generated by Django 3.0.7 on 2020-07-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0266_auto_20200719_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(default='2020-07-19 16:13:56'),
        ),
    ]
