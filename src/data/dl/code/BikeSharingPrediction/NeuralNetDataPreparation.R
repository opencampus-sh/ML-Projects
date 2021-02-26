
###################################################
### Preparation of the Environment ####

# Clear environment
remove(list = ls())

# Create list with needed libraries
pkgs <- c("readr", "fastDummies")

# Load each listed library and check if it is installed and install if necessary
for (pkg in pkgs) {
  if (!require(pkg, character.only = TRUE)) {
    install.packages(pkg)
    library(pkg, character.only = TRUE)
  }
}


###################################################
### Function Definition ####

#' Title Fast creation of normalized variables
#' Quickly create normalized columns from numeric type columns in the input data. This function is useful for statistical analysis when you want normalized columns rather than the actual columns.
#'
#' @param .data An object with the data set you want to make normalized columns from.
#' @param norm_values Dataframe of column names, means, and standard deviations that is used to create corresponding normalized variables from.
#'
#' @return A data.frame (or tibble or data.table, depending on input data type) with same number of rows an dcolumns as the inputted data, only with normalized columns for the variables indicated in the norm_values argument.
#' @export
#'
#' @examples
norm_cols <- function (.data, norm_values = NULL) {
  for (i in 1:nrow(norm_values)  ) {
    .data[[norm_values$name[i]]] <- (.data[[norm_values$name[i]]] - norm_values$mean[i]) / norm_values$sd[i]
  }
  return (.data)
}


#' Title Creation of a Dataframe including the Information to Standardize Variables
#' This function is meant to be used in combination with the function norm_cols
#'
#' @param .data A data set including the variables you want to get the means and standard deviations from.
#' @param select_columns A vector with a list of variable names for which you want to get the means and standard deviations from.
#'
#' @return A data.frame (or tibble or data.table, depending on input data type) including the names, means, and standard deviations of the variables included in the select_columns argument.
#' @export
#'
#' @examples
get.norm_values <- function (.data, select_columns = NULL) {
  result <- NULL
  for (col_name in select_columns) {
    mean <- mean(.data[[col_name]], na.rm = TRUE)
    sd <- sd(.data[[col_name]], na.rm = TRUE)
    result <- rbind (result, c(mean, sd))
  }
  result <- as.data.frame(result, stringsAsFactors = FALSE)
  result <- data.frame (select_columns, result, stringsAsFactors = FALSE)
  names(result) <- c("name", "mean", "sd")
  return (result)
}



###################################################
### Data Import ####

# Reading the data file
#house_pricing <- read_csv("https://raw.githubusercontent.com/opencampus-sh/sose20-datascience/master/house_pricing_test.csv")
bike_data <- read_csv("Daten/EnrichedData.csv")
#bike_data <- read_csv("Daten/Data_HbfUmsteiger.csv")
#bakery_earnings <- bakery_earnings %>% drop_na()

###################################################
### Data Preparation ####

# Recoding of the variables into one-hot encoded (dummy) variables
dummy_list <- c("is_weihnachten", "is_streiktag", "is_wochenende" ,"Wochentag")
#house_pricing_dummy = dummy_cols(house_pricing, dummy_list)
bike_data_dummy=dummy_cols(bike_data, dummy_list)

# Definition of lists for each one-hot encoded variable (just to make the handling easier)
#condition_dummies = c('condition_1', 'condition_2', 'condition_3', 'condition_4', 'condition_5')
#view_dummies = c('view_0', 'view_1', 'view_2', 'view_3','view_4')
is_weihnachten_dummies=c('is_weihnachten_0','is_weihnachten_1')
is_wochenende_dummies=c('is_wochenende_0','is_wochenende_1')
is_streiktag_dummies<-c('is_streiktag_0','is_streiktag_1')
Wochentag_dummies<-c('Wochentag_Dienstag','Wochentag_Donnerstag','Wochentag_Freitag',
'Wochentag_Mittwoch','Wochentag_Montag','Wochentag_Samstag', 'Wochentag_Sonntag')
bikes_rented_names<-c("bikes_rented", "bikes_rented_01", "bikes_rented_02", "bikes_rented_03", 
                      "bikes_rented_04",
                   "bikes_rented_05", "bikes_rented_06","bikes_rented_07", "bikes_rented_08",
                   "bikes_rented_09", "bikes_rented_10", "bikes_rented_11", "bikes_rented_12",
                   "bikes_rented_13", "bikes_rented_14", "bikes_rented_15", "bikes_rented_16", 
                   "bikes_rented_17", "bikes_rented_18",
                   "bikes_rented_19", "bikes_rented_20","bikes_rented_21", "bikes_rented_22",
                   "bikes_rented_23", "bikes_rented_24", "bikes_rented_25", "bikes_rented_26",
                   "bikes_rented_27", "bikes_rented_28")
bikes_returned_names<-c("bikes_returned", "bikes_returned_01", "bikes_returned_02", "bikes_returned_03", 
                      "bikes_returned_04",
                      "bikes_returned_05", "bikes_returned_06","bikes_returned_07", "bikes_returned_08",
                      "bikes_returned_09", "bikes_returned_10", "bikes_returned_11", "bikes_returned_12",
                      "bikes_returned_13", "bikes_returned_14", "bikes_returned_15", "bikes_returned_16", 
                      "bikes_returned_17", "bikes_returned_18",
                      "bikes_returned_19", "bikes_returned_20","bikes_returned_21", "bikes_returned_22",
                      "bikes_returned_23", "bikes_returned_24", "bikes_returned_25", "bikes_returned_26",
                      "bikes_returned_27", "bikes_returned_28")

# Standardization of all variables (features and label)
#norm_list <- c("price", "sqft_lot", "bathrooms", "grade", "waterfront", view_dummies, condition_dummies) # list of all relevant variables
#norm_values_list <- get.norm_values(house_pricing_dummy, norm_list)    # Calculation of the means and standard deviations
#house_pricing_norm <- norm_cols(house_pricing_dummy, norm_values_list) # Standardization of the variables
# norm_list <- c("SumUmsatzNeu", "UmsatzWG1", "UmsatzWG2", "UmsatzWG3", "UmsatzWG4", 
#                "UmsatzWG5","UmsatzWG6", 
#                "SumUmsatzNeu_1", "UmsatzWG1_1", "UmsatzWG2_1", "UmsatzWG3_1", "UmsatzWG4_1", 
#                "UmsatzWG5_1","UmsatzWG6_1", 
#                "SumUmsatzNeu_2", "UmsatzWG1_2", "UmsatzWG2_2", "UmsatzWG3_2", "UmsatzWG4_2", 
#                "UmsatzWG5_2","UmsatzWG6_2",
#                "SumUmsatzNeu_3", "UmsatzWG1_3", "UmsatzWG2_3", "UmsatzWG3_3", "UmsatzWG4_3", 
#                "UmsatzWG5_3","UmsatzWG6_3",
#                "SumUmsatzNeu_4", "UmsatzWG1_4", "UmsatzWG2_4", "UmsatzWG3_4", "UmsatzWG4_4", 
#                "UmsatzWG5_4","UmsatzWG6_4",
#                "SumUmsatzNeu_5", "UmsatzWG1_5", "UmsatzWG2_5", "UmsatzWG3_5", "UmsatzWG4_5", 
#                "UmsatzWG5_5","UmsatzWG6_5",
#                "SumUmsatzNeu_6", "UmsatzWG1_6", "UmsatzWG2_6", "UmsatzWG3_6", "UmsatzWG4_6", 
#                "UmsatzWG5_6","UmsatzWG6_6",
#                "SumUmsatzNeu_7", "UmsatzWG1_7", "UmsatzWG2_7", "UmsatzWG3_7", "UmsatzWG4_7", 
#                "UmsatzWG5_7","UmsatzWG6_7",is_silvester_dummies, KielerWoche_dummies) # list of all relevant variables
norm_list<-c(bikes_rented_names, bikes_returned_names ,is_weihnachten_dummies,
             is_streiktag_dummies,is_wochenende_dummies, Wochentag_dummies)
norm_values_list <- get.norm_values(bike_data_dummy, norm_list)    # Calculation of the means and standard deviations
bike_data_norm <- norm_cols(bike_data_dummy, norm_values_list) # Standardization of the variables




###################################################
### Selection of the Feature Variables and the Label Variable ####

# Selection of the features (the independent variables used to predict the dependent)
# features <-  c("UmsatzWG1_1", "UmsatzWG2_1", "UmsatzWG3_1", "UmsatzWG4_1", 
#                "UmsatzWG5_1","UmsatzWG6_1", 
#                "UmsatzWG1_2", "UmsatzWG2_2", "UmsatzWG3_2", "UmsatzWG4_2", 
#                "UmsatzWG5_2","UmsatzWG6_2",
#                "UmsatzWG1_3", "UmsatzWG2_3", "UmsatzWG3_3", "UmsatzWG4_3", 
#                "UmsatzWG5_3","UmsatzWG6_3",
#                "UmsatzWG1_4", "UmsatzWG2_4", "UmsatzWG3_4", "UmsatzWG4_4", 
#                "UmsatzWG5_4","UmsatzWG6_4",
#                "UmsatzWG1_5", "UmsatzWG2_5", "UmsatzWG3_5", "UmsatzWG4_5", 
#                "UmsatzWG5_5","UmsatzWG6_5",
#                "UmsatzWG1_6", "UmsatzWG2_6", "UmsatzWG3_6", "UmsatzWG4_6", 
#                "UmsatzWG5_6","UmsatzWG6_6",
#                "UmsatzWG1_7", "UmsatzWG2_7", "UmsatzWG3_7", "UmsatzWG4_7", 
#                "UmsatzWG5_7","UmsatzWG6_7",is_silvester_dummies, KielerWoche_dummies)
#from pacf(data$UmsatzWG1) # WG1 2,3,5,7,14
#from pacf(data$UmsatzWG2) # WG2 1,6,7,8
#from pacf(data$UmsatzWG3) # WG3 1,6,7,8
#from pacf(data$UmsatzWG4) # WG4 1,7,14
#from pacf(data$UmsatzWG5) # WG5 1,2,6,7
#from pacf(data$UmsatzWG6) # WG6 1,2,3,4,5
#adjusted 14.01.2021
#from pacf(data$UmsatzWG1) # WG1 1,2,3,5,6,7,14
#from pacf(data$UmsatzWG2) # WG2 1,6,7,8,9
#from pacf(data$UmsatzWG3) # WG3 1,6,7,8,9
#from pacf(data$UmsatzWG4) # WG4 1,7,9,14
#from pacf(data$UmsatzWG5) # WG5 1,2,6,7
#from pacf(data$UmsatzWG6) # WG6 1,2,3,4,5,11


bikes_rented_features<-c("bikes_rented_01", "bikes_rented_02", "bikes_rented_03", 
                         "bikes_rented_04", "bikes_rented_05", "bikes_rented_06","bikes_rented_07", 
                         "bikes_rented_08", "bikes_rented_09", "bikes_rented_10", "bikes_rented_11", 
                         "bikes_rented_12", "bikes_rented_13", "bikes_rented_14", "bikes_rented_15", 
                         "bikes_rented_16", "bikes_rented_17", "bikes_rented_18",
                         "bikes_rented_19", "bikes_rented_20","bikes_rented_21", "bikes_rented_22",
                         "bikes_rented_23", "bikes_rented_24", "bikes_rented_25", "bikes_rented_26",
                         "bikes_rented_27", "bikes_rented_28")
bikes_returned_features<-c("bikes_returned_01", "bikes_returned_02", "bikes_returned_03", 
                           "bikes_returned_04", "bikes_returned_05", "bikes_returned_06",
                           "bikes_returned_07", "bikes_returned_08", "bikes_returned_09", 
                           "bikes_returned_10", "bikes_returned_11", "bikes_returned_12",
                           "bikes_returned_13", "bikes_returned_14", "bikes_returned_15", 
                           "bikes_returned_16", "bikes_returned_17", "bikes_returned_18",
                           "bikes_returned_19", "bikes_returned_20", "bikes_returned_21", 
                           "bikes_returned_22", "bikes_returned_23", "bikes_returned_24", 
                           "bikes_returned_25", "bikes_returned_26", 
                           "bikes_returned_27", "bikes_returned_28")


#features<-c(bikes_rented_features, bikes_returned_features, is_weihnachten_dummies,
#            is_streiktag_dummies, is_wochenende_dummies)
features<-c(bikes_rented_features, bikes_returned_features, is_weihnachten_dummies,
            is_streiktag_dummies, Wochentag_dummies)

# Selection of the label (the dependent variable)
#labels <- c("SumUmsatzNeu", "UmsatzWG1", "UmsatzWG2", "UmsatzWG3", "UmsatzWG4",
#           "UmsatzWG5","UmsatzWG6")
#labels <- c("UmsatzWG5")
labels <- c("bikes_rented", "bikes_returned")
#Simpler Model

# Selection of the label (the dependent variable)
# labels <- c( "UmsatzWG1", "UmsatzWG2", "UmsatzWG3", "UmsatzWG4",
#            "UmsatzWG5")
# features <-  c("UmsatzWG1_1", "UmsatzWG2_1", "UmsatzWG3_1", "UmsatzWG4_1", 
#                "UmsatzWG5_1","UmsatzWG6_1", 
#                "SumUmsatzNeu_7", "UmsatzWG1_7", "UmsatzWG2_7", "UmsatzWG3_7", "UmsatzWG4_7", 
#                "UmsatzWG5_7","UmsatzWG6_7",is_silvester_dummies, KielerWoche_dummies)
# features <-  c("SumUmsatzNeu_1", "UmsatzWG1_1", "UmsatzWG2_1", "UmsatzWG3_1", "UmsatzWG4_1", 
# "UmsatzWG5_1","UmsatzWG6_1", 
# "SumUmsatzNeu_2", "UmsatzWG1_2", "UmsatzWG2_2", "UmsatzWG3_2", "UmsatzWG4_2", 
# "UmsatzWG5_2","UmsatzWG6_2",
# "SumUmsatzNeu_3", "UmsatzWG1_3", "UmsatzWG2_3", "UmsatzWG3_3", "UmsatzWG4_3", 
# "UmsatzWG5_3","UmsatzWG6_3",
# "SumUmsatzNeu_4", "UmsatzWG1_4", "UmsatzWG2_4", "UmsatzWG3_4", "UmsatzWG4_4", 
# "UmsatzWG5_4","UmsatzWG6_4",
# "SumUmsatzNeu_5", "UmsatzWG1_5", "UmsatzWG2_5", "UmsatzWG3_5", "UmsatzWG4_5", 
# "UmsatzWG5_5","UmsatzWG6_5",
# "SumUmsatzNeu_6", "UmsatzWG1_6", "UmsatzWG2_6", "UmsatzWG3_6", "UmsatzWG4_6", 
# "UmsatzWG5_6","UmsatzWG6_6",
# "SumUmsatzNeu_7", "UmsatzWG1_7", "UmsatzWG2_7", "UmsatzWG3_7", "UmsatzWG4_7", 
# "UmsatzWG5_7","UmsatzWG6_7",is_silvester_dummies, KielerWoche_dummies)


###################################################
### Selection of Training and Validation data ####

# Setting the random counter to a fixed value, so the random initialization stays the same (the random split is always the same)
set.seed(100)
# Generating the random indices for the training data set
train_ind <- sample(seq_len(nrow(bike_data_norm)), size = floor(0.8 * nrow(bike_data_norm)))

# Splitting the data into training and validation data and selecting the feature variables as a separate data frame
train_dataset = bike_data_norm[train_ind, features]
test_dataset = bike_data_norm[-train_ind, features]

# Splitting the data into training and validation data and selecting the label variable as a separate vector
train_labels = bike_data_norm[train_ind, labels]
test_labels = bike_data_norm[-train_ind, labels]


#strName<-"HBFUmsteiger"
strName<-"AlleStationen"
#write.csv(bike_data_norm,"Daten/NormierteDaten_AlleStationen.csv")
write.csv(bike_data_norm,paste0("Daten/NormierteDaten_", strName, ".csv"))
write.csv(train_dataset,paste0("Daten/TrainSet_",strName,".csv"))
write.csv(train_labels,paste0("Daten/TrainLabels_",strName,".csv"))
write.csv(test_dataset,paste0("Daten/TestSet_",strName,".csv"))
write.csv(test_labels,paste0("Daten/TestLabels_",strName,".csv"))
features
