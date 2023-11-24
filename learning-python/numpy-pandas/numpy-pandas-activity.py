### Working with Pandas ###
import numpy as np
import pandas as pd

## 1b: Read in file
# Read file and assign to top3
top3 = pd.read_csv('epa_ca_tx_pa.csv')

# Print first 5 rows
top3.head(5)

### Task 2: Summary Info ###
## 2a: Metadata ##
# Examine data such as number of rows, col, col names, data types and number of non-null values
top3.info()

## 2b: Summary statistics ##
# print statistics. with describe() method
top3.describe()

### Task 3: Explore Data ###
## 3a: Rows per state ##
# select state and values associated with that state
top3['state_name'].value_counts()   #top3.state_name.value_counts()

## 3b: Sort by AQI ##
# Create new data frame to sort top3 by AQI
top3_sorted = top3.sort_values(by=['aqi'], ascending=False)

# Print first 10 rows
top3_sorted.head(10)

## 3c: iloc to select rows ##
# find rows 10 and 11 **end index is not included in the range**
top3_sorted.iloc[10:12]

### Task 4: Examine California data ###
## 4a: Boolean Masking ##

# Create Boolean mask selects only observations of top3_sorted from Cali
ca_mask = top3_sorted['state_name'] == 'California'

# Apply Boolean mask to top3_sorted and assign to ca_df
ca_df = top3_sorted[ca_mask]

# Print first 5 rows of ca_df
ca_df.head(5)

## 4b: Validate CA data ##
#  inspect ca_df data
ca_df.shape     # (rows, columns)

## 4c: Rows per CA county ##
# find number of times a county appears
ca_df['county_name'].value_counts()

## 4d: Calculate mean AQI for LA county 
# boolean mask on ca_df to select LA County
la_mask = ca_df['county_name'] == 'Los Angeles'

# Apply Boolean mask to ca_df and assign to la_county
la_county = ca_df[la_mask] 

# calculate mean AQI for LA County
la_county['aqi'].mean()             # Could have done one liner: ca_df[la_mask]['aqi'].mean()

### Task 5: Groupby ###
# group top3 by state and calculate mean AQI for each state
top3.groupby('state_name').mean()['aqi']

### Task 6: Adding data ###
## 6a: Reading in other file ##
# read file to other_states
other_states = pd.read_csv('epa_others.csv')

# printfirst 5 rows
other_states.head(5)

## 6b: Concatenate data ##
# add data from other_states as new rows 
combined_df = pd.concat([top3, other_states], ignore_index=True)

# confirm len of combined is same as top3 plus other_states
if len(top3) + len(other_states) == len(combined_df):
    print(f"The combined data is the same as the sum of both individual data sets. \nTotal rows: {len(combined_df)}")
else:
    print(f"Data does not match: \ntop3: {len(top3)}\nother_states: {len(other_states)}\ncombined_df: {len(combined_df)}")

### Tasl 7: Complex Boolean masking ###
washington_mask = (combined_df['state_name'] == 'Washington') & (combined_df['aqi'] >= 51)

# Apply Boolean mask to ca_df and assign to la_county
moderate_aqi = combined_df[washington_mask]

# Print first few rows of data
moderate_aqi.head(25)

