
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
  ggplot(data = plot.data, aes(x = 1:13, y =net_cost_total)) + 
    geom_point() + geom_line() + expand_limits(y=0) +
    xlab("Time") + ylab("NET COST") + theme_bw() 
}

plot.multi.facet = function(plot.data)
{
  ggplot(data = plot.data, aes(x = period, y =net_cost_total/1000, colour = section)) + 
    geom_point(fill="black") + geom_line() + expand_limits(y=0) +
    xlab("Time") + ylab("NET COST (£000)") + theme_bw() + theme(legend.position="none") +
    facet_wrap(~section, ncol=1, scales = "free_y")
}

plot.multi.colour = function(plot.data)
{
  ggplot(data = plot.data, aes(x = period, y =net_cost_total/1000, colour = section)) + 
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

