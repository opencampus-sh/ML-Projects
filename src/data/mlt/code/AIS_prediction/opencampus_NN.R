library(data.table)
library(epitools)
library(tictoc)
getwd()
setwd("~/Projects/Export-Prediction")

# <- fread("input/container_vessel_positions/container_vessel_positions.csv")
#pcalls <- fread("container_vessel_portcalls/Container_Vessel_Portcalls_2020.csv") 
load("C:/Users/Steffen Gans/Documents/Projects/Export_Pred_NN/Shipping_Forecasting/input/pos_int1") # ship positions
load("C:/Users/Steffen Gans/Documents/Projects/Export_Pred_NN/Shipping_Forecasting/input/ships_fm") # ship information (sparse)
#load("input/calls20.csv")

# load model.matrix
#model.matrix <- fread("model.matrix.csv")

# load exports data
exports <- fread("Exports_SuJ.csv", header = T)
exports<- exports[1:(nrow(exports)-3),]
names(exports)[1:2] <- c("year", "month")
names(exports)[5] <- "Ausfuhr Dollar"

keep <- c("year", "month", "Ausfuhr Dollar")
exports <- exports[,..keep]
exports[month == "Januar", month.num := 01]
exports[month == "Februar", month.num := 02]
exports[month == "März", month.num := 03]
exports[month == "April", month.num := 04]
exports[month == "Mai", month.num := 05]
exports[month == "Juni", month.num := 06]
exports[month == "Juli", month.num := 07]
exports[month == "August", month.num := 08]
exports[month == "September", month.num := 09]
exports[month == "Oktober", month.num := 10]
exports[month == "November", month.num := 11]
exports[month == "Dezember", month.num := 12]

exports[month.num <10, date := paste0(year, "-", "0", month.num)]
exports[month.num >=10, date := paste0(year, "-", month.num) ]
exports[, month.num := NULL]

# change to pos later
pos[, timestamp_monthly := substr(timestamp, 1, 7)]

tic()
model.matrix <- merge.data.table(exports, pos, by.x = c("date"), by.y = c("timestamp_monthly"))
toc()
head(model.matrix)

# safe csv
write.csv(pos, "pos.csv")
# -----------------------------------------


## other stuff
year(pcalls[["time_arrival"]])

fishing <- fread("unknown.csv")

head(ships)
head(pos)

# 5615 ships
length(unique(pos[["IMO"]]))

# 5590224 uniquetimestamps
length(unique(pos[["timestamp"]]))

# 5590225 / 5614 ~ 1000 timestamps per ship ~ for each ship 3 years daily pos




load("ifw_trade")
head(ifw_trade)
tail(ifw_trade)
# try example with one imo

test <- ifw_trade[imo == 9859911,]

test[]




test <- pos[1:1000,]





# Start:

# |1| Try to extract gps (lat/long) from ship positions and project to raster -------------------------------------------------

# load ship positions
load("input/pos_int1")

# load raster
load("lc_layer")
load("lc_final")
load("id_layer")

#convert gps to cell_id
to_extract <- ships
coordinates(to_extract) <- ~long  + lat
proj4string(to_extract) <- CRS("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
to_extract <- spTransform(to_extract, proj4string(id_layer))
cell_ids<- extract(id_layer, to_extract)
ships[["cell_id"]]<- cell_ids

# load layers
load("id_layer")
# insert here: extracts from ship positions.


source("GCD.R")
load("cities_ports")
cities <- cities_ports





