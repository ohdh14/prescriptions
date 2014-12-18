
# Define UI for application that draws a histogram
shinyUI(fluidPage(theme = "bootstrap.css",
  
  # Application title
  titlePanel("Prescriptions Data Plotting"),
  
  # Sidebar with a slider input for the number of bins
  sidebarLayout(
    sidebarPanel(
      uiOutput("choose_section")
    ),
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("sectionPlot")
    )
  )
))

