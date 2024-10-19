import pandas as pd
import os

# Directory containing your cattle inventory CSV files
directory = r'<Your directory>/cattle_inventory'

# Initialize an empty dataframe to store the combined results
combined_df = pd.DataFrame()

# Loop through each file in the directory
for file in os.listdir(directory):
    if file.endswith('.csv'):
        # Load each CSV file
        df = pd.read_csv(os.path.join(directory, file))
        
        # Remove quotation marks from STATE_NAME if they exist
        df['STATE_NAME'] = df['STATE_NAME'].str.replace('"', '')
        
        # Combine the data into a single dataframe
        combined_df = pd.concat([combined_df, df])

# Group by the necessary columns and sum the total_cattle_inventory
summary_df = combined_df.groupby(
    ['YEAR', 'STATE_NAME', 'COMMODITY_DESC', 'STATISTICCAT_DESC', 'UNIT_DESC'],
    as_index=False
)['total_cattle_value'].sum()

# Save the summarized data to a new CSV file
summary_df.to_csv('summarized_cattle_inventory.csv', index=False)

print("Summarization complete. Saved to 'summarized_cattle_inventory.csv'")
