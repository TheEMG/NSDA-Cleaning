import pandas as pd
import os

# Directory containing your chicken production CSV files
directory = r'<your directory>\chicken_data_sample'

# Initialize an empty dataframe to store the combined results
combined_df = pd.DataFrame()

# Loop through each file in the directory
for file in os.listdir(directory):
    if file.endswith('.csv'):
        # Load each CSV file
        df = pd.read_csv(os.path.join(directory, file))
        
        # Remove US TOTAL and handle missing or empty STATE_NAME
        df = df[df['STATE_NAME'] != 'US TOTAL']
        df['STATE_NAME'] = df['STATE_NAME'].fillna('UNKNOWN')
        df['STATE_NAME'] = df['STATE_NAME'].replace('', 'UNKNOWN')
        
        # Remove rows where VALUE is '(D)'
        df = df[df['total_value'] != '(D)']
        
        # Combine the data into a single dataframe
        combined_df = pd.concat([combined_df, df])

# Group by the necessary columns and sum the total_value
summary_df = combined_df.groupby(
    ['YEAR', 'STATE_NAME', 'COMMODITY_DESC', 'STATISTICCAT_DESC', 'UNIT_DESC'],
    as_index=False
)['total_value'].sum()

# Save the summarized data to a new CSV file
summary_df.to_csv('summarized_chicken_production.csv', index=False)

print("Summarization complete. Saved to 'summarized_chicken_production.csv'")
