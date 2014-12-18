#' ---
#' title: "NHS prescription Analysis Aug 2013-2014"
#' author: "Matt Weller"
#' date: "Dec 14th, 2014"
#' ---
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

# set up the environment: clear, libraries, source functions
rm(list=ls())
library(data.table) ; require(stringr) ; library(ggplot2) ; library(bit64) ; library(knitr)
source("pca_analysis_functions.R")
opts_chunk$set(eval = FALSE, echo = FALSE)

# paramters
sections.filter = c("Antidepressant Drugs","Drugs Used In Diabetes", "Antihist, Hyposensit & Allergic Emergen", "Cough Preparations")
pth.data = "~/data/prescriptions/"
opt.agg = FALSE ; opt.save = FALSE

# get the data/aggregate the data/save the data/
if (opt.agg == FALSE) {
  dat = load.pca.data(opt.all = TRUE)
  # create data by SECTION
  dat.section = agg.pca.section.month(dat,opt.save = opt.save)
  # summarise by
  dat.summary = agg.pca.section(dat)
} else {
  dat = load.pca.data(opt.all = TRUE)
  dat.section = load.pca.section.month()
  dat.summary = agg.pca.section(dat)
}

dat.summary
# unique codes, sections, drugs (related reference data)
codes = length(unique(dat$code))
drugs = unique(dat[,list(section, chemical, drug)])
sections = unique(dat.section$section)
periods = data.table(period_date=unique(dat.section$period_date),period = 0,key = "period_date")[,period:=1:.N]

section.top30 = dat.summary$section[1:30]

# now print the outputs
print(head(dat.summary,3))
plot.top30.dotplot()
plot.top30.box()
print(plot1(data.monthly()))
print(plot.multi.facet(data.monthly(sections.filter)))
print(plot.multi.facet(data.monthly(section.top30[1:16])))
print(plot.multi.colour(data.monthly(sections.filter)))
print(plot.multi.colour(data.monthly(section.top30[1:16])))
plot.drug(drug.name = "Trifluoperazine_Tab 5mg")
filter.drug()
