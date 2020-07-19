# Generated by Django 3.0.8 on 2020-07-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20200709_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiomics_study',
            name='images_file_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-09 21:35:39'),
        ),
    ]
