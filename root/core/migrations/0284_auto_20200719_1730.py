# Generated by Django 3.0.7 on 2020-07-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0283_auto_20200719_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(default='2020-07-19 17:30:41'),
        ),
    ]
