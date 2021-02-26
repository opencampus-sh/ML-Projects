library(reticulate)
library(ggplot2)
library(Metrics)
library(data.table)
library(lubridate)
library(dprep)

getwd()
setwd("~/Projects/Export-Prediction")

#exports <- fread("exports_ifw.csv")
exports_ifw <- fread("exports_ifw_mly.csv")
exports[, V1 := NULL]
exports[, month := as.character(month)]
exports[, month_num := as.numeric(month)]
exports[month_num <10 , month := paste0("0", month)]
exports[, timestamp := as.character(paste0(year, "-",month))]
setcolorder(exports, "timestamp")



#exports[, timestamp := paste0(mday, ".", month, ".", year)]
#exports[,timestamp := as.Date(timestamp, format = "%d.%m.%Y")]





model.matrix = fread("model.matrix_new.csv")
model.matrix = model.matrix[order(timestamp),]
model.matrix[, V1 := NULL]

subset = c("timestamp", "ausfuhr_dollar")
y = model.matrix[, ..subset]
y = y[!duplicated(timestamp),]
y[, timestamp := as.Date(timestamp)]

y = y[, timestamp := substr(timestamp, 1,7)]
y = y[!duplicated(timestamp),]
#exports[, V1 := NULL]


exports = merge.data.table(exports, y, by = "timestamp")
#exports[, ausfuhr_dollar := ausfuhr_dollar.x]
#exports[, ausfuhr_dollar.x := NULL]
#exports[, ausfuhr_dollar.y := NULL]
exports[, month_num := NULL]
exports[, year := NULL]
exports[, month := NULL]

setcolorder(exports, c("timestamp", "ausfuhr_dollar"))
#exports = exports[!2,]
#setcolorder(exports, neworder = c("timestamp", "ausfuhr_dollar"))



exports[is.na(exports)] = 0
names(exports)
#exports = as.matrix(exports)

#for (column in names(exports)[5:length(names(exports))]){
 # print(column)
  #apply(exports[[column]], normalize)
#}

#exports[2, ausfuhr_dollar]

#names(exports)
#exports[1,1] = 0
#sapply(exports[,1], normalize)

exports[, year := NULL]
exports[, month := NULL]
exports[, mday := NULL]
setcolorder(exports, c("timestamp","ausfuhr_dollar"))

#getwd()
#write.csv(exports, "exports_ifw.csv")

#head(model.matrix)


#for (j in 1:nrow(exports)){
  #print(j)
 # exports[j, ][[column]] = (exports[j,][[column]] - min(exports[[column]]))/(max(exports[[column]])-min(exports[[column]]))
#}

head(exports)

normalize <- function(x)
{
  return((x- min(x)) /(max(x)-min(x)))
}
exports[is.na(exports),] = 0

timestamp = exports[, as.character(timestamp)]
exports = apply(exports[,2:ncol(exports)], MARGIN = 2, FUN= normalize)
exports = cbind(timestamp, exports)

exports = as.data.table(exports)
write.csv(exports, "exports_ifw_mly_norm.csv")




model.matrix <- fread("model.matrix_new.csv")
model.matrix <- model.matrix[,c("timestamp", "Ausfuhr Dollar", "imo", "speed", "course", "latitude", "longitude", "length", "draught", "width")]






#head(test.matrix)

model.matrix[, timestamp := substr(timestamp, 1, 10)]

model.matrix[, sum.ships := length(unique(imo)), by = c("year", "month")]
setcolorder(model.matrix, c("timestamp", "year", "month"))
names(model.matrix)
model.matrix[, date := NULL]
# amount of observations per timestamp
ship.obs <- unique(test.matrix[["sum.ships"]])
#ship.obs <- ship.obs[1:561]

# delete last obs with only few obs
model.matrix = model.matrix[!sum.ships == 299,]

# find min # of observations for timestamp
#min(ship.obs) # 3965

#min.ships <- test.matrix[sum.ships == 3965, imo]

#test.matrix <- test.matrix[imo %in% min.ships, ]


write.csv(model.matrix, "model.matrix_new.csv")
# ---------------------------------------------


# load
model.matrix <- fread("model.matrix_new.csv")

# some adjustments (for model.matrix_new!)
model.matrix[, V1 := NULL]


names(model.matrix)
setnames(model.matrix, "Ausfuhr Dollar", "ausfuhr_dollar")

model.matrix = na.omit(model.matrix)

# normalize
model.matrix[, ausfuhr_dollar :=  (ausfuhr_dollar- min(ausfuhr_dollar))/(max(ausfuhr_dollar)-min(ausfuhr_dollar))]
model.matrix[, imo := (imo- min(imo))/(max(imo)-min(imo))]
model.matrix[, speed :=  (speed- min(speed))/(max(speed)-min(speed))]
model.matrix[, course :=  (course- min(course))/(max(course)-min(course))]
model.matrix[, latitude := (latitude- min(latitude))/(max(latitude)-min(latitude)) ]
model.matrix[, longitude := (longitude- min(longitude))/(max(longitude)-min(longitude)) ]
model.matrix[, length :=  (length- min(length))/(max(length)-min(length))]
model.matrix[, draught :=  (draught- min(draught))/(max(draught)-min(draught))]
model.matrix[, width :=  (width- min(width))/(max(width)-min(width))]
model.matrix[, sum.ships :=  (sum.ships- min(sum.ships))/(max(sum.ships)-min(sum.ships))]
head(model.matrix)

write.csv(model.matrix, "model.matrix_new.csv")
#----------------------------------------------

names(model.matrix)

max(model.matrix[, speed])





max(model.matrix[["timestamp"]])


time.stamps = unique(model.matrix[,timestamp])


wrapper = matrix(nrow = 2125, ncol = 1)



for (i in 1:2125) {
  assign(paste("matrix",i,sep=""), model.matrix[timestamp == time.stamps[i],])
  
}








for (i in 1:2125){
  wrapper[i] = paste0("matrix", i)
}

for (target_matrix in wrapper){
  target_matrix = model.matrix[timestamp == time.stamps[i],]
  return(target_matrix)
}

for (target_matrix in wrapper){
  print(target_matrix)
}

a = array(0, c(3,3,3))
write.csv(a, "a.csv")

names(model.matrix)

lab.index = model.matrix[, c("timestamp", "Ausfuhr Dollar")]
lab.index = unique(lab.index)


write.csv(lab.index, "lab.index.csv")
