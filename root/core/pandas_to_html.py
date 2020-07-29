
def df_to_html(df):
    cell_properties = [('font-size', '10pt')]
    styles = [dict(selector='td', props=[('max-width', '100px')]),
              dict(selector="tr", props=cell_properties)]

    df = df[['study_name', 'study_creator', 'study_description', 'imaging_type', 'creation_date',
             'ROI_name', 'features_family', 'num_patients', 'eval_features', 'download_features', 'delete_study']]
    df = df.style.hide_index().set_table_styles(styles).set_table_attributes('border="1" class="table table-hover"').set_properties(**
                                                                                                                                    {'margin-left': '-120px', 'border-collapse': 'collapse', 'font-size': '12pt', 'font-family': 'Calibri', 'max-width': '100', 'text-align': 'center'}).render()
    return df
