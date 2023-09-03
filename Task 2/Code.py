# Load the necessary packages from the tidyverse collection
library(dplyr)
library(tidyr)
library(purrr)

# Define the analyse_and_fit_lrm() function
analyse_and_fit_lrm <- function(dataset_path) {
  # Read the dataset from the provided path (assuming it's a tab-separated file)
  data <- read.delim(dataset_path)
  
  # Step 1: Calculate Statistics
  # Filter data for houses with two bathrooms and four bedrooms
  filtered_data <- data %>% filter(Bathroom == 2, Bedroom == 4)
  
  # Calculate statistics for the TAX variable
  statistics <- c(
    mean(filtered_data$Tax),
    sd(filtered_data$Tax),
    median(filtered_data$Tax),
    min(filtered_data$Tax),
    max(filtered_data$Tax)
  )
  
  # Step 2: Create Data Frame
  # Filter data for houses with Space greater than 800 and order by Price in decreasing order
  data_frame <- data %>% filter(Space > 800) %>% arrange(desc(Price))
  
  # Step 3: Calculate Number of Observations
  # Calculate the 4th quintile of the Lot variable
  quantile_value <- quantile(data$Lot, probs = 0.8)
  
  # Count observations where Lot is equal to or greater than the 4th quintile
  num_observations <- sum(data$Lot >= quantile_value)
  
  # Step 4: Build Linear Regression Model
  # Fit a linear regression model to predict Price based on other variables
  lm_model <- lm(Price ~ Bedroom + Space + Room + Lot + Tax + Bathroom + Garage + Condition, data)
  
  # Step 5: Make Price Prediction
  # Create a data frame with specific parameters for prediction
  new_data <- data.frame(
    Bedroom = 3,
    Space = 1500,
    Room = 8,
    Lot = 40,
    Tax = 1000,
    Bathroom = 2,
    Garage = 1,
    Condition = 0
  )
  
  # Predict the price using the linear regression model
  price_prediction <- predict(lm_model, new_data)
  
  # Create and return the summary list and regression list
  summary_list <- list(
    Statistics = statistics,
    Data_frame = data_frame,
    Number_of_observations = num_observations
  )
  
  regression_list <- list(
    Model_parameters = coef(lm_model),
    Price_prediction = price_prediction
  )
  
  return(list(Summary_list = summary_list, Regression_list = regression_list))
}

# Example usage:
dataset_path <- "C:/Users/jillbair/Downloads/house_data.tsv"
result <- analyse_and_fit_lrm(dataset_path)
print(result)
