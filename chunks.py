import csv
import os

# Using the output from the process_large_dataset.py (qs.animals_products_20240814_filtered.csv) we can now create 
# manageable chunks of size 500,000 entries per csv files.

def split_and_filter_csv(input_file, output_dir, delimiter=',', chunk_size=500000):
    # Desired columns based on what's need in my analysis, this can change depending on who ever is using this this dataset.
    desired_columns = [
        'SOURCE_DESC', 'SECTOR_DESC', 'GROUP_DESC', 'COMMODITY_DESC', 'CLASS_DESC',
        'PRODN_PRACTICE_DESC', 'UTIL_PRACTICE_DESC', 'STATISTICCAT_DESC', 'UNIT_DESC', 
        'SHORT_DESC', 'DOMAIN_DESC', 'DOMAINCAT_DESC', 'AGG_LEVEL_DESC', 
        'STATE_NAME', 'COUNTY_NAME', 'REGION_DESC', 'LOCATION_DESC', 
        'YEAR', 'FREQ_DESC', 'VALUE', 'CV_%'
    ]

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile, delimiter=delimiter)
        
        # Read the header and map columns
        header = next(reader)
        header_map = {col: i for i, col in enumerate(header)}

        missing_columns = [col for col in desired_columns if col not in header_map]
        if missing_columns:
            print(f"Warning: The following columns are missing in the file and will be filled with empty values: {missing_columns}")

        chunk_number = 1
        chunk = []
        
        for row in reader:
            # Create a standardized row with the desired columns
            standardized_row = [row[header_map[col]] if col in header_map and len(row) > header_map[col] else '' for col in desired_columns]
            chunk.append(standardized_row)
            
            if len(chunk) >= chunk_size:
                output_file = os.path.join(output_dir, f'qs_animals_products_chunk_{chunk_number}.csv')
                with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(desired_columns)  # Write header
                    writer.writerows(chunk)
                print(f'Created {output_file}')
                chunk_number += 1
                chunk = []  # Reset chunk
        
        # Save any remaining rows in the last chunk
        if chunk:
            output_file = os.path.join(output_dir, f'qs_animals_products_chunk_{chunk_number}.csv')
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(desired_columns)  # Write header
                writer.writerows(chunk)
            print(f'Created {output_file}')

input_file = 'qs.animals_products_20240814_filtered.csv'
output_dir = 'data_chunks' # CHANGE TO YOUR DIRECTORY 

split_and_filter_csv(input_file, output_dir)
