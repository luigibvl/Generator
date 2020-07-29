from django.http import HttpResponse
from .models import Features_Model


def download_features(request, radiomics_study_id):

    download_file = get_csv_file(radiomics_study_id)
    response = HttpResponse(content_type='text/csv')
    file_name = 'features_study.csv'
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    response.write(download_file)
    return response


def get_csv_file(radiomics_study_id):

    features_model = Features_Model.objects.get(
        study_id=radiomics_study_id)

    features = features_model.data
    csv_data = features.to_csv()
    return csv_data
