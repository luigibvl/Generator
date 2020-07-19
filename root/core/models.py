from django.db import models
from datetime import datetime
from time import strftime
from django import forms
from multiselectfield import MultiSelectField
from picklefield.fields import PickledObjectField



IMAGING_TYPE_CHOISES = (
    ('mri t1', 'MRI T1'),
    ('mri t2', 'MRI T2'),
    ('dwi', 'DWI'),
    ('ct', 'CT'),
)

FEATURES_FAMILY_CHOISES = (
    ('stat', 'Statistical'),
    ('morph', 'Morphological'),
    ('glcm', 'Texture GLCM'),
    ('rlm', 'Texture RLM'),
    ('szm', 'Texture SZM'),
)


class Features_Model(models.Model):

    features_id = models.AutoField(primary_key=True)
    study_id = models.CharField(max_length=100)
    data = PickledObjectField()

    def __str__(self):
        return self.features_id



class Radiomics_Study(models.Model):

    study_id = models.AutoField(primary_key=True)
    study_name = models.CharField(max_length=100)
    study_creator = models.CharField(max_length=100)
    study_description = models.CharField(max_length=1000)
    imaging_type = models.CharField(
        max_length=6, choices=IMAGING_TYPE_CHOISES, default='mri t1')
    creation_date = models.DateTimeField(
        default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    ROI_name = models.CharField(max_length=100)
    features_family = MultiSelectField(
        max_length=23, choices=FEATURES_FAMILY_CHOISES, default=('stat', 'morph', 'glcm', 'rlm', 'szm'), max_choices=5)
    num_patients = models.IntegerField(default=-1)
    images_path = models.CharField(max_length=100)
    images_file_name = models.CharField(max_length=100)
    eval_features = models.CharField(max_length=100)
    download_features = models.CharField(max_length=17, default='download_features')
    delete_study = models.CharField(max_length=12)


    def __str__(self):
        return self.study_name
