from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Radiomics_Study
import pandas as pd
from .pandas_to_html import df_to_html


#################### VISUALIZE STUDIES ######################


@login_required
def all_studies(request):

    df = pd.DataFrame.from_records(
        Radiomics_Study.objects.filter(study_creator=request.user.username)
        .order_by('study_id').values())

    if not df.empty:
        df = df_to_html(df)
        return render(request, 'all_studies.html', {'Radiomics_Studies': df})
    return render(request, 'all_studies.html')


@login_required
def sort_df_date_ascending(request):
    df = pd.DataFrame.from_records(
        Radiomics_Study.objects.filter(study_creator=request.user.username)
        .order_by('creation_date').values())

    if not df.empty:
        df = df_to_html(df)
        return render(request, 'all_studies.html', {'Radiomics_Studies': df})
    return render(request, 'all_studies.html')



@login_required
def sort_df_date_descending(request):
    df = pd.DataFrame.from_records(
        Radiomics_Study.objects.filter(study_creator=request.user.username)
        .order_by('-creation_date').values())

    if not df.empty:
        df = df_to_html(df)
        return render(request, 'all_studies.html', {'Radiomics_Studies': df})
    return render(request, 'all_studies.html')



@login_required
def sort_df_num_patients_descending(request):
    df = pd.DataFrame.from_records(
        Radiomics_Study.objects.filter(study_creator=request.user.username)
        .order_by('-num_patients').values())

    if not df.empty:
        df = df_to_html(df)
        return render(request, 'all_studies.html', {'Radiomics_Studies': df})
    return render(request, 'all_studies.html')


@login_required
def sort_df_num_patients_ascending(request):
    df = pd.DataFrame.from_records(
        Radiomics_Study.objects.filter(study_creator=request.user.username)
        .order_by('num_patients').values())

    if not df.empty:
        df = df_to_html(df)
        return render(request, 'all_studies.html', {'Radiomics_Studies': df})
    return render(request, 'all_studies.html')
