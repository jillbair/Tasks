# Task 1: CSV Data Processing

## Task Description
Your task is to prepare a function that extracts, summarizes, and exports information from CSV files containing historical prices of traded shares of fictional companies. The CSV files are located in the /data/ folder and have the following structure:

- date: Specific trading date in the format 'YYYY-MM-DD'
- open, max, min, close: Opening, maximum, minimum, and closing prices, respectively
- vol: Volume (number of shares traded during a given day)

The function should return a list of nested lists. Each nested list consists of two data frames with aggregated data for the individual company:

### First Data Frame: Highest Trading Volume Values in Individual Years
- Columns:
  - date: The date of the day with the highest trading volume in a year (parsed as a datetime in 'YYYY-MM-DD' format)
  - vol: The actual volume of shares traded on that day
- The number of rows in the data frame should be equal to the number of years in the history of the given company.

### Second Data Frame: Days of Highest Closing Prices in Individual Years
- Columns:
  - date: The date of the day with the highest closing prices in a year (parsed as a datetime in 'YYYY-MM-DD' format)
  - close: The actual closing price
- If the same closing price occurred on more than one day in a given year, include them all with their full dates.
- The number of rows in the data frame might be greater than the equivalent dimension for the first data frame.

## Approach
Explain the approach you took to solve this task. You can provide a high-level overview of your code's logic and the libraries you used (e.g., pandas, numpy).

## Usage
If applicable, explain how to run your code. Provide instructions on how to use the function you created to process CSV data.

## Sample Output
If you have sample output or results from running your code, you can include a section with a brief example.

## Files
List the important files in this task, such as code.py, data files, or any other relevant files.

