from .adapter import Adapter
from django.conf import settings
from rpy2.robjects import pandas2ri
import rpy2.robjects as ro
from rpy2.robjects.conversion import localconverter
from .models import Radiomics_Study, Features_Model
from django.contrib import messages


def make_features_from_r(adapter, path, images_path, roi_name, features_family):
    adapter.source(path)
    features_family_list = [x for x in features_family]
    features = adapter.extract_features(
        images_path, roi_name, features_family_list)
    del adapter
    return features


def make_features(radiomics_study_id, images_path, ROI_name, features_family):

    adapter = Adapter()

    features = make_features_from_r(
        adapter.r_adapter, settings.MODDICOM_FILE, images_path, ROI_name, features_family)

    print('--------------------------')
    print('End of feature calculation')
    print('--------------------------')

    download_features = "<a href='http://localhost:8000/download_features/" + \
        str(radiomics_study_id) + "'>download_features</a>"

    Radiomics_Study.objects.filter(study_id=radiomics_study_id).update(
        download_features=download_features)

    with localconverter(ro.default_converter + pandas2ri.converter):
        pd_from_r_df = ro.conversion.rpy2py(features)

    if Features_Model.objects.filter(study_id=radiomics_study_id).exists():
        Features_Model.objects.filter(
            study_id=radiomics_study_id).update(data=pd_from_r_df)
    else:
        features_model = Features_Model(
            study_id=radiomics_study_id, data=pd_from_r_df)
        features_model.save()
