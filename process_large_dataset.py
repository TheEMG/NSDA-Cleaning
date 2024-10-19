import csv

# Serves to reduce the the 3.5GB File -> 2.5GB 
# Note: Be sure to check the read me to access this file from the USDA website, the file is to big to attach to github

def convert_to_csv(input_file, output_file, delimiter='\t', chunk_size=10**6):
    # Desired columns based on the first header row you provided
    desired_columns = [
        'SOURCE_DESC', 'SECTOR_DESC', 'GROUP_DESC', 'COMMODITY_DESC', 'CLASS_DESC',
        'PRODN_PRACTICE_DESC', 'UTIL_PRACTICE_DESC', 'STATISTICCAT_DESC', 'UNIT_DESC', 
        'SHORT_DESC', 'DOMAIN_DESC', 'DOMAINCAT_DESC', 'AGG_LEVEL_DESC', 
        'STATE_NAME', 'COUNTY_NAME', 'REGION_DESC', 'LOCATION_DESC', 
        'YEAR', 'FREQ_DESC', 'VALUE', 'CV_%'
    ]

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter=delimiter)
        writer = csv.writer(outfile)

        # Write the standardized header
        writer.writerow(desired_columns)

        # Read the first line to determine the header
        header = next(reader)
        header_map = {col: i for i, col in enumerate(header)}

        # Ensure all desired columns exist in the current header
        missing_columns = [col for col in desired_columns if col not in header_map]
        if missing_columns:
            print(f"Warning: The following columns are missing in the file and will be filled with empty values: {missing_columns}")

        while True:
            chunk = [next(reader, None) for _ in range(chunk_size)]
            chunk = [row for row in chunk if row is not None]
            if not chunk:
                break

            for row in chunk:
                # Create a standardized row with the desired columns
                standardized_row = [row[header_map[col]] if col in header_map and len(row) > header_map[col] else '' for col in desired_columns]
                writer.writerow(standardized_row)

input_file = 'qs.animals_products_20240814.txt'
output_file = 'qs.animals_products_20240814_filtered.csv'

convert_to_csv(input_file, output_file)
