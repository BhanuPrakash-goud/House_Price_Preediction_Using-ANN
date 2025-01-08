import pandas as pd

# Read the four CSV files
df_hyderabad=pd.read_csv('Hyderabad1.csv')
df_warangal = pd.read_csv('warangal_dataset.csv')
df_khammam = pd.read_csv('khammam_dataset.csv')
df_karimnagar = pd.read_csv('karimnagar_dataset.csv')

# Add a 'District' column to each DataFrame
df_hyderabad['District'] = 'Hyderabad'
df_warangal['District'] = 'Warangal'
df_khammam['District'] = 'Khammam'
df_karimnagar['District'] = 'Karimnagar'  # Assuming Buppalapally is a district

# Concatenate the DataFrames
df_telangana = pd.concat([df_hyderabad, df_warangal, df_khammam, df_karimnagar], ignore_index=True)

# Save the merged DataFrame to a CSV file
df_telangana.to_csv('telangana_dataset.csv', index=False)
