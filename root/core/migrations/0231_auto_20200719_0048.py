# Generated by Django 3.0.7 on 2020-07-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0230_auto_20200719_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(default='2020-07-19 00:48:17'),
        ),
    ]
