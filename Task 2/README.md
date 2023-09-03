# Task 2: Analyze Data and Apply Linear Regression Model

## Task Description
In this task, you are required to analyze a dataset containing information about house prices in California and apply a linear regression model to understand the relationship between the price of houses (dependent variable) and various predictor variables. The dataset consists of the following variables:
- Price: Price of the house
- Bedroom: Number of bedrooms
- Space: Space of the house
- Room: Number of rooms
- Lot: Width of the lot
- Tax: Amount of annual tax
- Bathroom: Number of bathrooms
- Garage: Number of parking spaces
- Condition: Condition of the house (1 if good, 0 otherwise)

You need to perform data analysis, calculate statistics, and build a linear regression model to predict house prices.

## Function: `analyse_and_fit_lrm()`
Write a function named `analyse_and_fit_lrm()` that takes one argument, a path to a dataset, and returns a named list of the following objects:

### Summary_list (named list of length 3):
1. **Statistics**: A numeric vector of length 5 specifying mean, standard deviation, median, minimum, and maximum for the variable TAX for all houses with two bathrooms and four bedrooms (you do not need to name elements of the vector).
2. **Data_frame**: A data frame with observations for which the Space is greater than 800, ordered in decreasing order of Price.
3. **Number_of_observations**: A numeric value corresponding to the number of observations for which the value of the variable "Lot" is equal to or greater than the 4th quintile of this variable.

### Regression_list (named list of length 2):
1. **Model_parameters**: A numeric vector of length 9 giving the model parameters. The first element of the vector should be named "Intercept," and all other elements should have the same name as the respective variable.
2. **Price_prediction**: A numeric value corresponding to the prediction of the price (using the applied model) for a house with specific parameters: three bedrooms; 1500 square feet of space; eight rooms; width of lot is 40; $1000 tax; two bathrooms; one space in the garage; the house is in bad condition.

## Dataset Sample
The dataset is tab-separated and contains nine columns: Price, Bedroom, Space, Room, Lot, Tax, Bathroom, Garage, and Condition. Below is a sample of the dataset:

