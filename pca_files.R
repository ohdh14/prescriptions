
rm(list=ls())
library(data.table)
require(stringr)
pth.data = "~/data/prescriptions/"

files = grep(".csv|.CSV", dir(pth.data),value = TRUE)
SUBS = NULL
BNFT = NULL

myfread = function (fil)  {
  print(fil)
  dat = fread(paste0(pth.data , fil))
  period = substr(fil, 2, 7)
  data.table(period = period, dat)[, lapply(.SD,str_trim)]
}

SUBS = rbindlist(lapply(grep("SUBS", files, value = TRUE ), myfread))
BNFT = rbindlist(lapply(grep("ADDR BNFT", files, value = TRUE ), myfread))

names.BNFT = c("V1", "period", "prac_id", "prac_name", "add_1", "add_2", "town", "county", "postcode")
setnames(BNFT, names.BNFT)
BNFT[, V1:=NULL]
names.SUBS = c("period", "subs_id", "subs_name", "other")
setnames(SUBS, names.SUBS)


postcodes = data.table(postcode = unique(BNFT$postcode))
#postcodes[, c("postcode_district", "postcode_area", "postcode_sector") := list(f)]
postcodes[, `:=` (lat = 0, lon = 0)]
write.csv(postcodes, file=paste0(pth.data, "postcodes.csv"), row.names=FALSE)
x=read.csv(file=paste0(pth.data,"postcodes.csv"))
