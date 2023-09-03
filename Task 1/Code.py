import os
import pandas as pd

def extract_aggregated_data(user_folder, csv_files):
    aggregated_data = []
    
    for csv_file in csv_files:
        # Create the full file path for the CSV file
        file_path = os.path.join(user_folder, csv_file)
        
        # Check if the file exists
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue
        
        # Extract the company name from the file name (excluding the file extension)
        company_name = os.path.splitext(os.path.basename(csv_file))[0]
        
        try:
            # Load the CSV data into a DataFrame
            df = pd.read_csv(file_path)
            
            # Convert the 'date' column to a datetime object
            df['date'] = pd.to_datetime(df['date'])
            
            # Group data by year and find the day with the highest trading volume
            highest_volume_data = df.groupby(df['date'].dt.year)['vol'].idxmax()
            highest_volume_df = df.loc[highest_volume_data, ['date', 'vol']]
            
            # Group data by year and find the days with the highest closing prices
            highest_closing_data = df.groupby(df['date'].dt.year)['close'].idxmax()
            highest_closing_df = df.loc[highest_closing_data, ['date', 'close']]
            
            # Append the dataframes to the aggregated_data list
            aggregated_data.append([highest_volume_df, highest_closing_df])
        
        except Exception as e:
            print(f"Error processing {csv_file}: {str(e)}")
    
    return aggregated_data

# Example usage:
user_folder = '/path/to/user/jillbair/Downloads'
csv_files = ['throwsh.csv', 'twerche.csv']

result = extract_aggregated_data(user_folder, csv_files)
print(result)
