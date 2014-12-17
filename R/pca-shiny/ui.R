library(shiny) ; library(data.table) ; require(stringr) ; library(ggplot2) ; library(bit64) ; library(knitr)
source("../pca_analysis_functions.R")

# paramters
sections.filter = c("Antidepressant Drugs","Drugs Used In Diabetes", "Antihist, Hyposensit & Allergic Emergen", "Cough Preparations")
pth.data = "/Users/Wellermatt/data/prescriptions/"
dat = load.pca.data(opt.all = TRUE)


# unique codes, sections, drugs (related reference data)
codes = length(unique(dat$code))
sections = unique(dat$section)
# Define UI for application that draws a histogram
shinyUI(fluidPage(theme = "bootstrap.css",
  
  # Application title
  titlePanel("Prescriptions Data Plotting"),
  
  # Sidebar with a slider input for the number of bins
  sidebarLayout(
    sidebarPanel(
      selectInput("section", label = h3("Section"), 
                  choices = list(sections))),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("sectionPlot")
    )
  )
))