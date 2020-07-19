
#import threading
from .make_features import make_features
from celery import shared_task
from django.contrib import messages
from celery_progress.backend import ProgressRecorder
import time
import os
from .models import Radiomics_Study
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect


@shared_task(bind=True)
def start_task(self, percentage, radiomics_study_id, images_path, ROI_name, features_family):

    result = 0
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        if i==0:
            make_features(radiomics_study_id, images_path, ROI_name, features_family)
        result += i
        progress_recorder.set_progress(i + 1, percentage)

    progress_recorder.set_progress(10, percentage)
    return result


# def create_radiomic_study(form, file_name, username, radiomics_images):
#     t = threading.Thread(target=create_thread_radiomic_study, args=(
#         form, file_name, username, radiomics_images,))
#     t.setDaemon(False)
#     t.start()
