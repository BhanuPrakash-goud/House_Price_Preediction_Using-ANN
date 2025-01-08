import pandas as pd
import numpy as np

# Define the data
data_karimnagar = {
    'Area': [1300, 1500, 1700, 1900, 1100, 1300, 1500, 1700, 1900, 1200, 1400, 1600, 1800, 2000, 1400, 1600,1500],
    'Price': [5000000, 5500000, 6000000, 6500000, 4500000, 5200000, 5800000, 6200000, 6800000, 4700000, 5400000, 
              6000000, 6500000, 7000000, 5500000, 6000000, 6500000],  # Adjusted length for Buppalapally
    'Location': ['Jagityal', 'Huzurabad', 'Manakondur', 'Korutla', 'Siricilla', 'Karimnagar', 'Jagityal', 
                 'Huzurabad', 'Manakondur', 'Korutla', 'Siricilla', 'Karimnagar', 'Jagityal', 'Huzurabad', 
                 'Manakondur', 'Korutla', 'Buppalapally'],  # Added Buppalapally
    'No. of Bedrooms': [3, 3, 4, 4, 2, 3, 3, 4, 4, 2, 3, 3, 4, 4, 3, 3, 3],  # Adjusted length for Buppalapally
    'Resale': np.random.randint(0, 2, size=17),  # Adjusted size for Buppalapally
    'MaintenanceStaff': np.random.randint(0, 2, size=17),
    'Gymnasium': np.random.randint(0, 2, size=17),
    'SwimmingPool': np.random.randint(0, 2, size=17),
    'LandscapedGardens': np.random.randint(0, 2, size=17),
    'JoggingTrack': np.random.randint(0, 2, size=17),
    'RainWaterHarvesting': np.random.randint(0, 2, size=17),
    'IndoorGames': np.random.randint(0, 2, size=17),
    'ShoppingMall': np.random.randint(0, 2, size=17),
    'Intercom': np.random.randint(0, 2, size=17),
    'SportsFacility': np.random.randint(0, 2, size=17),
    'ATM': np.random.randint(0, 2, size=17),
    'ClubHouse': np.random.randint(0, 2, size=17),
    'School': np.random.randint(0, 2, size=17),
    '24X7Security': np.random.randint(0, 2, size=17),
    'PowerBackup': np.random.randint(0, 2, size=17),
    'CarParking': np.random.randint(0, 2, size=17),
    'StaffQuarter': np.random.randint(0, 2, size=17),
    'Cafeteria': np.random.randint(0, 2, size=17),
    'MultipurposeRoom': np.random.randint(0, 2, size=17),
    'Hospital': np.random.randint(0, 2, size=17),
    'WashingMachine': np.random.randint(0, 2, size=17),
    'Gasconnection': np.random.randint(0, 2, size=17),
    'AC': np.random.randint(0, 2, size=17),
    'Wifi': np.random.randint(0, 2, size=17),
    'ChildrensPlayArea': np.random.randint(0, 2, size=17),
    'LiftAvailable': np.random.randint(0, 2, size=17),
    'BED': np.random.randint(0, 2, size=17),
    'VaastuCompliant': np.random.randint(0, 2, size=17),
    'Microwave': np.random.randint(0, 2, size=17),
    'GolfCourse': np.random.randint(0, 2, size=17),
    'TV': np.random.randint(0, 2, size=17),
    'DiningTable': np.random.randint(0, 2, size=17),
    'Sofa': np.random.randint(0, 2, size=17),
    'Wardrobe': np.random.randint(0, 2, size=17),
    'Refrigerator': np.random.randint(0, 2, size=17)
}

# Create DataFrame for Karimnagar
df_karimnagar = pd.DataFrame(data_karimnagar)

# Save DataFrame to CSV
df_karimnagar.to_csv('karimnagar_dataset.csv', index=False)
