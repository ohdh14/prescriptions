

# script for analysing the aggregated prescriptions data
# dimensions: 
#  - drug (section, chemical, drug, ADD generic/branded ADD prep class, std qty unit)
#  - dispensing outlet type (Pharmacy/non-pharmacy)
#  - time (month, quarter)
#  - class (1 or 2)
# measures:
#  - items dispensed
#  - cost
#  - quantity
# calculated measures:
#  - 

rm(list=ls())
library(data.table) ; require(stringr) ; library(ggplot2) ; library(bit64)
source("pca_analysis_functions.R")
# paramters
sections.filter = c("Antidepressant Drugs", "Antihist, Hyposensit & Allergic Emergen", "Cough Preparations")

# load the data and rename/columns as required
pth.data = "~/data/prescriptions/"
dat = readRDS(paste0(pth.data, "pca_all.rds"))
setnames(dat, names(dat)[1:4], c("code","section", "chemical", "drug"))

# add all of the calculated fields
dat[, net_cost_class2 := net_cost_class2/100]
dat[, net_cost := net_cost/100]
dat[, class2_share_qty:=(quantity_class2/quantity)]
dat[, class2_share_cost:=(net_cost_class2/net_cost_class2)]

# unique codes, sections, drugs (related data)
codes = length(unique(dat$code))
sections = unique(dat$section)
drugs = unique(dat[,list(section, chemical, drug)])
time.periods = c(201308:201312, 201401:201408)
periods = data.table(period_date=unique(dat$period_date),period = 1:13,key = "period_date")


# create data by section
dat.section = dat[, list(net_cost = sum(net_cost)/1000), by = c("section", "period_date")]
dat.summary = dat.section[j = list(net_cost_total = sum(net_cost),
                                   cost_max = max(net_cost),
                                   cost_min = min(net_cost),
                                   cost_range = max(net_cost) - min(net_cost),
                                   cost_mean = mean(net_cost),
                                   cost_sd = sd(net_cost),
                                   cost_cov = sd(net_cost)/mean(net_cost)), 
                          by = section][order(-net_cost_total)]
dat.summary[, cost_rank := 1:.N]
print(dat.summary)
section.top30 = dat.summary$section[1:30]

plot.top30.dotplot()
plot.top30.box()
print(plot1(data.monthly()))
print(plot.multi.facet(data.monthly(sections.filter)))
print(plot.multi.colour(data.monthly(sections.filter)))
plot.drug()
filter.drug()

