import pandas as pd

# Load the CSV file with semicolon delimiter
data = pd.read_csv('/Volumes/My Passport/vesha designs/amenities.csv', delimiter=';')

# Print column names to check
print(data.columns)

# Rename columns based on actual names
data.rename(columns={'unified_id': 'id', 'month': 'month', 'hot_tub': 'hot_tub', 'pool': 'pool'}, inplace=True)

# Convert 'month' to datetime format
data['month'] = pd.to_datetime(data['month'])

# Aggregate data: Count number of listings with pool or hot tub each month
monthly_data = data.groupby('month').agg({
    'pool': 'sum',      # Total listings with a pool
    'hot_tub': 'sum'    # Total listings with a hot tub
}).reset_index()

# Rename columns for Prophet
monthly_data.rename(columns={'month': 'ds', 'pool': 'y'}, inplace=True)

# Save the processed data to a new CSV file
monthly_data.to_csv('/Volumes/My Passport/vesha designs/processed_amenities.csv', index=False)

print("Data processed and saved to 'processed_amenities.csv'.")
