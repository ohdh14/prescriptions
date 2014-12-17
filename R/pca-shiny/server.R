library(shiny) ; library(data.table) ; require(stringr) ; library(ggplot2) ; library(bit64) ; library(knitr)

source("../pca_analysis_functions.R")

# paramters
sections.filter = c("Antidepressant Drugs","Drugs Used In Diabetes", "Antihist, Hyposensit & Allergic Emergen", "Cough Preparations")
pth.data = "/Users/Wellermatt/data/prescriptions/"
dat = load.pca.data(opt.all = TRUE)


# unique codes, sections, drugs (related reference data)
codes = length(unique(dat$code))
sections = unique(dat$section)
drugs = unique(dat[,list(section, chemical, drug)])
periods = data.table(period_date=unique(dat$period_date),period = 0,key = "period_date")[,period:=1:.N]

# create data by SECTION
dat.section = dat[, list(net_cost = sum(net_cost)/1000), 
                  by = c("section", "period_date")]

# summarise by sections
dat.summary = agg.pca(dat)




# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
  # Expression that generates a histogram. The expression is
  # wrapped in a call to renderPlot to indicate that:
  #
  #  1) It is "reactive" and therefore should re-execute automatically
  #     when inputs change
  #  2) Its output type is a plot
  
  output$sectionPlot <- renderPlot({
    plot.multi.facet(plot.data = data.monthly(sections.filter))
  })
})