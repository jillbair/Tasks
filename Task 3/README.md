Task 3: Calculating 1-Minute VWAP at 10:30 AM
Description
This task involves writing a Python program to calculate the 1-minute VWAP (Volume-Weighted Average Price) at 10:30 AM using trading data stored in a numpy dataframe named DATA_P. The 10:30 AM data is represented by the 60th row of DATA_P for simplicity.

Context
Sam, a day trader, plans to use the VWAP indicator to enhance his day trading performance. The VWAP is a popular indicator used by traders to assess the average price at which a security has traded throughout the day, weighted by trading volume.

Data Structure
The structure of the DATA_P dataframe is as follows:

Date	Open	Highest	Lowest	Close	Volume
9.30	79.85	81	78.65	79.9	42,191,984
9.31	79.85	81	78.65	79.9	42,191,984
9.32	80	80	77	79.85	45,300,436
9.33	74.05	76.65	72.75	75	51,884,797
9.34	75.3	75.9	71.55	72.55	50,134,617
...	...	...	...	...	...
Program Usage
To calculate the 1-minute VWAP at 10:30 AM, you can use the provided Python program. Follow the steps below:

Load your trading data into a numpy dataframe named DATA_P.
Use the program to calculate the 1-minute VWAP at 10:30 AM by referring to the 60th row of the dataframe.
Example Python code:

python
Copy code
import numpy as np

# Load your trading data into a numpy dataframe named DATA_P

# Calculate the 1-minute VWAP at 10:30 AM
vwap_1030 = np.average(DATA_P["Close"][:60], weights=DATA_P["Volume"][:60])

print(f"1-Minute VWAP at 10:30 AM: {vwap_1030}")
Make sure to replace "DATA_P" with your actual numpy dataframe containing the trading data.

Note
Ensure that you have the necessary trading data loaded into the DATA_P dataframe before running the program. The program calculates the VWAP using the "Close" prices and "Volume" data for the first 60 minutes of trading. Adjust the code as needed for your specific dataset and requirements.

