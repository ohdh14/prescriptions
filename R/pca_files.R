# this file 
rm(list=ls())
library(data.table) ; require(stringr) ; require(bit64)
pth.data = "~/data/prescriptions/"

myfread = function(fil) {
  fil = paste0(pth.data, fil)
  dat = fread(fil)  
  dat
}


dat = myfread(fil = "pca_files/aggregated_pca_09_14.csv")
dat$'Net Ingredient Cost of which Class 2' = NULL
setcolorder(dat,c(2,3,1,4,9,12,5,6,10,11,7,8,13,14))
new.names = c("code", "section", "chemical", "drug", "prep_class", "std_qty_unit", 
              "items_dispensed", "items_class2", "quantity", "quantity_class2", 
              "net_cost", "net_cost_class2", "period_date", "worksheet")
setnames(dat, new.names)
saveRDS(dat, "~/data/prescriptions/pca_files/pca_all_2009_2014.rds")



files = grep(".csv|.CSV", dir(pth.data),value = TRUE)

SUBS = NULL ; BNFT = NULL
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
