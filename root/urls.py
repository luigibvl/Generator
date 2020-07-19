from django.contrib import admin
from django.urls import re_path, path, include
from django.conf import settings
from django.conf.urls.static import static
from root.user import views as user_views
from root.core import views as core_views
from root.core import filtering_views as core_filtering_views
from root.core import sorting_views as core_sorting_views
from root.core import download_features



urlpatterns = [

    re_path(r'^celery-progress/', include('celery_progress.urls')),

    path('', user_views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('delete_account/', user_views.delete_account, name='delete_account'),
    path('create_study/', core_views.create_study, name='create_study'),

    path('all_studies/', core_sorting_views.all_studies, name='all_studies'),
    path('sort_df_date_ascending/', core_sorting_views.sort_df_date_ascending, name='sort_df_date_ascending'),
    path('sort_df_date_descending/', core_sorting_views.sort_df_date_descending, name='sort_df_date_descending'),
    path('sort_df_num_patients_ascending/', core_sorting_views.sort_df_num_patients_ascending, name='sort_df_num_patients_ascending'),
    path('sort_df_num_patients_descending/', core_sorting_views.sort_df_num_patients_descending, name='sort_df_num_patients_descending'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('evaluate/<str:radiomics_study_id>/', core_views.evaluation_features),
    path('delete/<str:radiomics_study_id>/', core_views.delete_study),
    path('download_features/<str:radiomics_study_id>/', download_features.download_features,name='download_features'),

    path('study_filter_by_name/', core_filtering_views.study_filter_by_name, name='study_filter_by_name'),
    path('study_filter_by_ROI_name/', core_filtering_views.study_filter_by_ROI_name, name='study_filter_by_ROI_name'),
    path('study_filter_by_imaging_type/', core_filtering_views.study_filter_by_imaging_type, name='study_filter_by_imaging_type'),
    path('reset_filters/', core_filtering_views.reset_filters, name='reset_filters'),
    path('study_filter_by_features_family/', core_filtering_views.study_filter_by_features_family, name='study_filter_by_features_family'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
