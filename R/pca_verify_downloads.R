library(data.table) ; library(foreach)
files = dir("~/data/prescriptions/pca_files/")

dates = foreach (fil = files, .combine = function(x,y)rbindlist(list(x,y))) %do% {
  print(fil)
  x = strsplit(fil, "[.]")[[1]][1]
  dat = strsplit(x, "_")[[1]][2:3]
  data.table(MMM = dat[1], YY = dat[2])
}

dates[YY==11]
table(dates$YY)
