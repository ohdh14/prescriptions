
load.pca.data = function(opt.all = FALSE) {
  
  # load the data and rename/columns as required
  if (opt.all == FALSE) {
    dat = readRDS(paste0(pth.data, "pca_files/pca_all_original.rds"))
    setnames(dat, names(dat)[1:4], c("code","section", "chemical", "drug"))
    new.names = names(dat)
  } else {
    dat = readRDS(paste0(pth.data, "pca_files/pca_all_2009_2014.rds"))[,period_date := as.Date(period_date)]
    sapply(dat,class)
    #dat = dat[period_date >= '2011-01-01 00:00:00']
  }
  
  # add all of the calculated fields
  dat[, net_cost_class2 := net_cost_class2/100]
  dat[, net_cost := net_cost/100]
  dat[, class2_share_qty:=(quantity_class2/quantity)]
  dat[, class2_share_cost:=(net_cost_class2/net_cost_class2)]
  dat
}

agg.pca = function(dat) {
  
  dat.summary = dat.section[j = list(net_cost_total = sum(net_cost),
                                     cost_max = max(net_cost),
                                     cost_min = min(net_cost),
                                     cost_range = max(net_cost) - min(net_cost),
                                     cost_mean = mean(net_cost),
                                     cost_median = median(net_cost),
                                     cost_sd = sd(net_cost),
                                     cost_cov = sd(net_cost)/mean(net_cost)), 
                            by = section][order(-net_cost_total)]
  dat.summary[, cost_rank := 1:.N]
  dat.summary
}


plot.top30.dotplot = function() {
  ggplot(dat.summary[cost_rank<=30], aes(y = reorder(section, net_cost_total), x = net_cost_total/1000)) + 
    geom_point() + xlab("Net Cost (£m)") + ylab("") + expand_limits(x=0)  +
    theme_bw() + ggtitle("Top 30 Sections by Total Cost (13 months)")  
}


plot.top30.box = function() {
  ggplot(dat.section[section %in% section.top30], aes(x = reorder(section, net_cost), y = net_cost/1000)) + 
    geom_boxplot() + ylab("\nNet Cost (£m)") + xlab("") + expand_limits(x=0)  +
    theme_bw() + ggtitle("Top 30 Sections: Monthly Cost Distributions\n") + coord_flip()  
}


data.monthly = function(section="Cough Preparations")
{
  if (length(section)==1){
    par.section = section
    dat.monthly = dat[section==par.section, list(net_cost_total = sum(net_cost)),by = c("section", "period_date")]
  } else {
    sections.filter = section
    dat.monthly = dat[section %in% sections.filter , list(net_cost_total = sum(net_cost)), by = c("section","period_date")]
  }
  setkeyv(dat.monthly, "period_date")
  dat.monthly[periods]
}

plot1 = function(plot.data)
{  
  ggplot(data = plot.data, aes(x = period_date, y =net_cost_total)) + 
    geom_point() + geom_line() + expand_limits(y=0) +
    xlab("Time") + ylab("NET COST") + theme_bw() 
}

plot.multi.facet = function(plot.data)
{
  ggplot(data = plot.data, aes(x = period_date, y =net_cost_total/1000, colour = section)) + 
    geom_point(fill="black") + geom_line() + expand_limits(y=0) +
    xlab("Time") + ylab("NET COST (£000)") + theme_bw() + theme(legend.position="none") +
    facet_wrap(~section, scales = "free_y")
}

plot.multi.colour = function(plot.data)
{
  ggplot(data = plot.data, aes(x = period_date, y =net_cost_total/1000, colour = section)) + 
    geom_point(fill="black") + geom_line() + expand_limits(y=0) +
    xlab("Time") + ylab("NET COST (£000)") + theme_bw() + theme(legend.position="top")
}

filter.drug = function(fltr ="Trifluoperazine_Tab 5mg")
{
  #drugs = grep("Trifluoperazine",unique(dat$drug), value = TRUE)
  dat.tf =  dat[drug == fltr]
  dat.tf[,list(net_cost_total = sum(net_cost)), by = period_date][order(period_date)]
}

plot.drug = function(drug.name = "Trifluoperazine_Tab 5mg") 
{
  plot.data = filter.drug(drug.name)
  plot1(plot.data)
}

