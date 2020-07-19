# Generated by Django 3.0.7 on 2020-07-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200705_1742'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.RenameField(
            model_name='radiomics_study',
            old_name='radiomics_images',
            new_name='radiomics_images_path',
        ),
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-05 19:53:51'),
        ),
    ]
