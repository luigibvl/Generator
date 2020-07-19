
library(moddicom)

extract_features <- function (path, roi, features_family) {

  images_path <- path

  roi_name <- roi

  features <- f.extractor.sing.par(path = images_path, ROIName = roi_name, feature.family = features_family)

  return(features)

}
