import numpy as np
import pandas as pd

# Define the user's folder and file name
user_folder = "/Users/jillbair/Downloads"
file_name = "your_dataset.csv"  # Replace with your actual dataset file name

# Construct the full file path
file_path = f"{user_folder}/{file_name}"

# Load the dataset into a pandas DataFrame
data = pd.read_csv(file_path)

# Assuming the 10:30 AM data is represented by the 60th row
data_1030 = data.iloc[59]

# Calculate the 1-minute VWAP at 10:30 AM
vwap_1030 = sum(data_1030['Close'] * data_1030['Volume']) / sum(data_1030['Volume'])

print(f"1-Minute VWAP at 10:30 AM: {vwap_1030}")
