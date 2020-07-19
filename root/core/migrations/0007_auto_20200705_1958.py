# Generated by Django 3.0.7 on 2020-07-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200705_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radiomics_study',
            old_name='radiomics_images_path',
            new_name='images_path',
        ),
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-05 19:58:39'),
        ),
    ]
