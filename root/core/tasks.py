
from .make_features import make_features
from celery import shared_task
from celery_progress.backend import ProgressRecorder
from .models import Radiomics_Study


@shared_task(bind=True)
def eval_features(self, percentage, radiomics_study_id, images_path, ROI_name, features_family):

    result = 0
    progress_recorder = ProgressRecorder(self)
    radiomic_study = Radiomics_Study.objects.get(study_id=radiomics_study_id)
    num_patients = radiomic_study.num_patients

    for i in range(5):
        if i == 0:
            if num_patients > 0:
                make_features(radiomics_study_id, images_path,
                              ROI_name, features_family)
            else:
                raise Exception("Sorry, there are no patients here")
        result += i
        progress_recorder.set_progress(i + 1, percentage)

    progress_recorder.set_progress(10, percentage)
    return result
