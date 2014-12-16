# load and clean the raw csv/xls files


library(data.table)
library(ggplot2)
pth.data = "~/Data/prescriptions/"

fil = "raw-downloads/ccg-pres-data-jul-sep-2014-un-dat.csv"
raw = data.table(read.csv(paste0(pth.data,fil)))
period = "2014Q1"
names(raw)
setnames(chapter.summary, "BNF.Chapter.Name", "chapter")

head(raw,3)
summary(raw)


unique(raw[,j = list(BNF.Chapter.Name, BNF.Section.Name)])
unique(raw[,j = list(BNF.Chapter.Name)])

# chapter summary
chapter.summary = raw[,j = list(cost = sum(Actual.Cost), nic = sum(NIC)), by = c("BNF.Chapter.Name",)][,nic_cost_ratio := nic/cost]


ggplot(raw, aes(y=Actual.Cost/1000, x=BNF.Chapter.Name)) + geom_boxplot() + coord_flip()
