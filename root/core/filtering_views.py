from .forms import Radiomics_Study_Form, Filter_Study_By_Name_Form, Filter_Study_By_ROI_Name_Form, Filter_Study_By_Imaging_Type_Form, Filter_Study_By_Features_Family_Form
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Radiomics_Study
import pandas as pd
from django.contrib import messages
from .pandas_to_html import df_to_html



#################### FILTER STUDY ########################



@login_required
def reset_filters(request):

    if request.method == 'GET':
        df = pd.DataFrame.from_records(Radiomics_Study.objects.filter(
            study_creator=request.user.username).order_by('study_id').values())
        if not df.empty:
            df = df_to_html(df)
            return render(request, 'all_studies.html', {'Radiomics_Studies': df})
        return redirect('all_studies')



@login_required
def study_filter_by_features_family(request):

    if request.method == 'POST':
        form = Filter_Study_By_Features_Family_Form(request.POST)

        if form.is_valid():
            features_family = form.cleaned_data.get('name_field')

            df = pd.DataFrame.from_records(Radiomics_Study.objects.filter(
                study_creator=request.user.username, features_family=features_family).order_by('study_id').values())

            if not df.empty:
                df = df_to_html(df)
                return render(request, 'all_studies.html', {'Radiomics_Studies': df})
        messages.warning(
            request, 'There is no Radiomic Study with this Features Family!')
        return redirect('all_studies')
    else:
        form = Filter_Study_By_Features_Family_Form()

    return render(request, 'study_filtering.html', {'form': form})


@login_required
def study_filter_by_imaging_type(request):

    if request.method == 'POST':
        form = Filter_Study_By_Imaging_Type_Form(request.POST)
        if form.is_valid():
            imaging_type = form.cleaned_data.get('name_field')

            df = pd.DataFrame.from_records(Radiomics_Study.objects.filter(
                study_creator=request.user.username, imaging_type=imaging_type).order_by('study_id').values())

            if not df.empty:
                df = df_to_html(df)
                return render(request, 'all_studies.html', {'Radiomics_Studies': df})
        messages.warning(
            request, 'There is no Radiomic Study with this Imaging Type name!')
        return redirect('all_studies')
    else:
        form = Filter_Study_By_Imaging_Type_Form()

    return render(request, 'study_filtering.html', {'form': form})


@login_required
def study_filter_by_name(request):

    if request.method == 'POST':
        form = Filter_Study_By_Name_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name_field')

            df = pd.DataFrame.from_records(Radiomics_Study.objects.filter(
                study_creator=request.user.username, study_name=name).order_by('study_id').values())

            if not df.empty:
                df = df_to_html(df)
                return render(request, 'all_studies.html', {'Radiomics_Studies': df})
        messages.warning(
            request, 'There is no Radiomic Study with this name!')
        return redirect('all_studies')
    else:
        form = Filter_Study_By_Name_Form()

    return render(request, 'study_filtering.html', {'form': form})


@login_required
def study_filter_by_ROI_name(request):

    if request.method == 'POST':
        form = Filter_Study_By_ROI_Name_Form(request.POST)
        if form.is_valid():
            roi_name = form.cleaned_data.get('name_field')

            df = pd.DataFrame.from_records(Radiomics_Study.objects.filter(
                study_creator=request.user.username, ROI_name=roi_name).order_by('study_id').values())

            if not df.empty:
                df = df_to_html(df)
                return render(request, 'all_studies.html', {'Radiomics_Studies': df})
        messages.warning(
            request, 'There is no Radiomic Study with this ROI name!')
        return redirect('all_studies')
    else:
        form = Filter_Study_By_ROI_Name_Form()

    return render(request, 'study_filtering.html', {'form': form})
