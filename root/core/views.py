from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Radiomics_Study, Features_Model
from .forms import Radiomics_Study_Form
import pandas as pd
from django.core.files.storage import FileSystemStorage
import os
import shutil
from .tasks import eval_features
from zipfile import ZipFile
from django.conf import settings
from django.contrib import messages
from django.db import transaction


#################### COMPUTE FEATURES ########################

@transaction.atomic
@login_required
def evaluation_features(request, radiomics_study_id):
    if request.method == 'GET':

        radiomics_study = Radiomics_Study.objects.get(
            study_id=radiomics_study_id)

        images_path = os.path.join(
            settings.BASE_DIR, radiomics_study.images_path, radiomics_study.images_file_name.split('.')[0])
        ROI_name = radiomics_study.ROI_name
        features_family = radiomics_study.features_family

        percentage = 100
        result = eval_features.delay(percentage, radiomics_study_id,
                                     images_path, ROI_name, features_family)
        messages.info(
            request, 'We are generating your features! Wait a while.')

        df = pd.DataFrame.from_records(Radiomics_Study.objects.filter(
            study_id=radiomics_study_id).values())

        df = df[['study_id', 'study_name', 'study_creator', 'study_description',
                 'imaging_type', 'creation_date', 'ROI_name', 'features_family', 'num_patients']]

        cell_properties = [('font-size', '10pt')]
        styles = [dict(selector='td', props=[('max-width', '100px')]),
                  dict(selector="tr", props=cell_properties)]
        df = df.style.hide_index().set_table_styles(styles).set_table_attributes('border="1" class="table table-hover"').set_properties(**
                                                                                                                                        {'margin-left': '-120px', 'border-collapse': 'collapse', 'font-size': '12pt', 'font-family': 'Calibri', 'max-width': '100', 'text-align': 'center'}).render()

        return render(request, 'evaluate.html', {'Radiomics_Study': df, 'radiomics_study_id': radiomics_study_id, 'task_id': result.task_id})


#################### DELETE STUDY ########################

@transaction.atomic
@login_required
def delete_study(request, radiomics_study_id):
    study_deleted = False
    if request.method == 'GET' or request.method == 'POST':

        if Radiomics_Study.objects.filter(study_id=radiomics_study_id).exists():
            radiomic_study = Radiomics_Study.objects.filter(
                study_id=radiomics_study_id)
            radiomic_study.delete()

        # elimino le immagini associate allo studio
        path = settings.MEDIA_ROOT + str(radiomics_study_id)

        if os.path.exists(path):
            shutil.rmtree(path)

        # elimino le feature (se calcolate) associate allo studio
        if Features_Model.objects.filter(study_id=radiomics_study_id).exists():
            features = Features_Model.objects.filter(
                study_id=radiomics_study_id)
            features.delete()
        
        study_deleted = True

    if request.method == 'GET' and study_deleted:
        return redirect('all_studies')


#################### CREATE STUDY ########################

@transaction.atomic
@login_required
def create_study(request):

    if request.method == 'POST':

        form = Radiomics_Study_Form(request.POST, request.FILES)
        if form.is_valid():

            try:
                messages.info(
                    request, 'We are generating your Radiomic Study! Wait a while.')

                radiomics_images = request.FILES.getlist('file_field')

                radiomics_study = form.save()

                evaluate_url = "<a href='http://localhost:8000/evaluate/" + \
                    str(radiomics_study.study_id) + "'>eval_features</a>"

                delete_study_url = "<a href='http://localhost:8000/delete/" + \
                    str(radiomics_study.study_id) + "'>delete_study</a>"

                Radiomics_Study.objects.filter(study_id=radiomics_study.study_id).update(
                    delete_study=delete_study_url)
                Radiomics_Study.objects.filter(study_id=radiomics_study.study_id).update(
                    study_creator=request.user.username)
                Radiomics_Study.objects.filter(study_id=radiomics_study.study_id).update(
                    eval_features=evaluate_url)
                Radiomics_Study.objects.filter(study_id=radiomics_study.study_id).update(
                    images_path=settings.MEDIA_URL + str(radiomics_study.study_id) + '/')

                if not os.path.exists(settings.MEDIA_ROOT):
                    os.mkdir(settings.MEDIA_ROOT)
                if not os.path.exists(settings.MEDIA_ROOT + str(radiomics_study.study_id)):
                    os.mkdir(settings.MEDIA_ROOT +
                             str(radiomics_study.study_id))

                path = settings.MEDIA_ROOT + str(radiomics_study.study_id)
                fs = FileSystemStorage(location=path)

                os.chdir(path)
                for f in radiomics_images:
                    fs.save(f.name, f)
                    with ZipFile(f.name, 'r') as zipObj:

                        extracted_names_list = zipObj.namelist()
                        extracted_name = extracted_names_list[0]
                        if extracted_name.endswith('/'):
                            extracted_name = extracted_name[:-1]
                        zipObj.extractall()
                        os.remove(f.name)

                    try:
                        num_patients = sum(os.path.isdir(os.path.join(path + '/' + str(extracted_name.split(
                            '.')[0]), i)) for i in os.listdir(path + '/' + str(extracted_name.split('.')[0])))
                    except:
                        num_patients = -1

                Radiomics_Study.objects.filter(study_id=radiomics_study.study_id).update(
                    images_file_name=extracted_name)
                Radiomics_Study.objects.filter(study_id=radiomics_study.study_id).update(
                    num_patients=num_patients)

                if num_patients == -1:
                    messages.error(request, 'There are no patients here!')
                    delete_study(request, radiomics_study.study_id)
                else:
                    messages.success(
                        request, 'We have created your Radiomic Study!')

                return redirect('create_study')
            except:
                messages.error(request, 'An Error occurred!')
                pass
    else:
        form = Radiomics_Study_Form()

    return render(request, 'create_study.html', {'form': form})
