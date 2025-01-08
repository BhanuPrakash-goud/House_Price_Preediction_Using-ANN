import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('telangana_dataset.csv')

# Reorder the columns as needed
new_column_sequence = ['District', 'Location', 'Area','Price', 'No. of Bedrooms', 
                      'Resale', 'MaintenanceStaff', 'Gymnasium', 'SwimmingPool', 
                      'LandscapedGardens', 'JoggingTrack', 'RainWaterHarvesting', 
                      'IndoorGames', 'ShoppingMall', 'Intercom', 'SportsFacility', 
                      'ATM', 'ClubHouse', 'School', '24X7Security', 'PowerBackup', 
                      'CarParking', 'StaffQuarter', 'Cafeteria', 'MultipurposeRoom', 
                      'Hospital', 'WashingMachine', 'Gasconnection', 'AC', 'Wifi', 
                      'Childrensplayarea', 'LiftAvailable', 'BED', 'VaastuCompliant', 
                      'Microwave', 'GolfCourse', 'TV', 'DiningTable', 'Sofa', 
                      'Wardrobe', 'Refrigerator']

df = df[new_column_sequence]

# Save the DataFrame back to a new CSV file
df.to_csv('Telangana.csv', index=False)
