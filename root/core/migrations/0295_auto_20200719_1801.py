# Generated by Django 3.0.7 on 2020-07-19 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0294_auto_20200719_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiomics_study',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
