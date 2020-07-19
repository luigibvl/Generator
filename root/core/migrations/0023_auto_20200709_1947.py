# Generated by Django 3.0.8 on 2020-07-09 19:47

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200709_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiomics_study',
            name='features_family',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('mri_t1', 'MRI T1'), ('mri_t2', 'MRI T2'), ('dwi', 'DWI'), ('ct', 'CT')], default='mri_t1', max_length=100),
        ),
        migrations.AlterField(
            model_name='radiomics_study',
            name='imaging_type',
            field=models.CharField(choices=[('mri_t1', 'MRI T1'), ('mri_t2', 'MRI T2'), ('dwi', 'DWI'), ('ct', 'CT')], default='mri_t1', max_length=6),
        ),
        migrations.AlterField(
            model_name='radiomics_study',
            name='study_creation_date',
            field=models.DateTimeField(default='2020-07-09 19:47:43'),
        ),
    ]
