
rm(list=ls())
library(data.table)
require(stringr)
pth.data = "~/data/prescriptions/"

require(bit64)
library(ggplot2)

dat = readRDS(paste0(pth.data, "pca_all.rds"))
setnames(dat, names(dat)[1:4], c("code","section", "chemical", "drug"))

dat[, net_cost_class2 := net_cost_class2/100]
dat[, net_cost := net_cost/100]
#dat[, period_date := as.Date(period_date, format = "%YYYY-%mm") ]

dat[, class2_share_qty:=(quantity_class2/quantity)]
dat[, class2_share_cost:=(net_cost_class2/net_cost_class2)]

names(dat)
sapply(dat,class)
codes = length(unique(dat$code))
sections = unique(dat$section)
periods = data.table(period_date=unique(dat$period_date),period = 1:13,key = "period_date")


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

ggplot(dat.summary[cost_rank<=30], aes(y = reorder(section, net_cost_total), x = net_cost_total)) + 
  geom_point() + theme_bw()


sections.filter = c("Antidepressant Drugs", 
                    "Antihist, Hyposensit & Allergic Emergen",
                    "Cough Preparations")

data.monthly = function(section="Cough Preparations")
{
  if (length(section)==1){
    dat.monthly = dat[section== "Cough Preparations" , 
                      list(net_cost_total = sum(net_cost)), 
                      by = period_date]
    
  } else {
    dat.monthly = dat[section %in% sections.filter , 
                      list(net_cost_total = sum(net_cost)), 
                      by = c("section","period_date")]
    
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
print(plot1(data.monthly()))

plot.multi.facet = function(plot.data)
{
  ggplot(data = plot.data, aes(x = period, y =net_cost_total/1000, colour = section)) + 
    geom_point(fill="black") + geom_line() + expand_limits(y=0) +
    xlab("Time") + ylab("NET COST (£000)") + theme_bw() + theme(legend.position="none") +
    facet_wrap(~section, ncol=1, scales = "free_y")
}
print(plot.multi.facet(data.monthly(sections.filter)))

