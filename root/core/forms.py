from django import forms
from .models import Radiomics_Study, IMAGING_TYPE_CHOISES, FEATURES_FAMILY_CHOISES
from django.forms import ModelForm


class Radiomics_Study_Form(ModelForm):
    file_field = forms.FileField(label="Choose study images in .zip", widget=forms.ClearableFileInput(
        attrs={'multiple': False, 'webkitdirectory': False, 'directory': False, 'accept': '.zip'}))

    class Meta:
        model = Radiomics_Study
        fields = ['study_name', 'study_description', 'imaging_type',
                  'ROI_name', 'features_family', 'file_field']




class Filter_Study_By_Name_Form(forms.Form):
    name_field = forms.CharField(max_length=100, label="Study Name")


class Filter_Study_By_ROI_Name_Form(forms.Form):
    name_field = forms.CharField(max_length=100, label="ROI Name")


class Filter_Study_By_Imaging_Type_Form(forms.Form):
    name_field = forms.CharField(
        max_length=100, label="Imaging Type", widget=forms.Select(choices=IMAGING_TYPE_CHOISES))


class Filter_Study_By_Features_Family_Form(forms.Form):
    name_field = forms.MultipleChoiceField(
        label="Features Family", required=True, widget=forms.CheckboxSelectMultiple(), choices=FEATURES_FAMILY_CHOISES)
