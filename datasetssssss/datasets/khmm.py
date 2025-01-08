import pandas as pd
import numpy as np

# Define the data
data_khammam = {
    'Area': [1400, 1600, 1800, 2000, 1500, 1700, 1900, 1300, 1700, 1500, 1800, 1200, 1400, 1600, 1800, 2000],
    'Price': [5500000, 6500000, 7500000, 8000000, 6000000, 7000000, 7500000, 5000000, 6500000, 5500000, 7000000, 4800000, 5200000, 6000000, 7000000, 8000000],
    'Location': ['Srinivasa Nagar', 'Gandhi Chowk', 'Lakshmipuram', 'Buddhavarapu Nagar', 'Narsimharaopeta', 
                 'Ramnagar', 'Ashok Nagar', 'Bhadrachalam Road', 'Nagulapalli', 'Gandhi Chowk', 
                 'Srinivasa Nagar', 'Lakshmipuram', 'Buddhavarapu Nagar', 'Ramnagar', 'Ashok Nagar', 
                 'Bhadrachalam Road'],
    'No. of Bedrooms': [3, 4, 4, 3, 3, 2, 4, 2, 3, 3, 4, 2, 3, 3, 4, 4],
    'Resale': np.random.randint(0, 2, size=16),
    'MaintenanceStaff': np.random.randint(0, 2, size=16),
    'Gymnasium': np.random.randint(0, 2, size=16),
    'SwimmingPool': np.random.randint(0, 2, size=16),
    'LandscapedGardens': np.random.randint(0, 2, size=16),
    'JoggingTrack': np.random.randint(0, 2, size=16),
    'RainWaterHarvesting': np.random.randint(0, 2, size=16),
    'IndoorGames': np.random.randint(0, 2, size=16),
    'ShoppingMall': np.random.randint(0, 2, size=16),
    'Intercom': np.random.randint(0, 2, size=16),
    'SportsFacility': np.random.randint(0, 2, size=16),
    'ATM': np.random.randint(0, 2, size=16),
    'ClubHouse': np.random.randint(0, 2, size=16),
    'School': np.random.randint(0, 2, size=16),
    '24X7Security': np.random.randint(0, 2, size=16),
    'PowerBackup': np.random.randint(0, 2, size=16),
    'CarParking': np.random.randint(0, 2, size=16),
    'StaffQuarter': np.random.randint(0, 2, size=16),
    'Cafeteria': np.random.randint(0, 2, size=16),
    'MultipurposeRoom': np.random.randint(0, 2, size=16),
    'Hospital': np.random.randint(0, 2, size=16),
    'WashingMachine': np.random.randint(0, 2, size=16),
    'Gasconnection': np.random.randint(0, 2, size=16),
    'AC': np.random.randint(0, 2, size=16),
    'Wifi': np.random.randint(0, 2, size=16),
    'ChildrensPlayArea': np.random.randint(0, 2, size=16),
    'LiftAvailable': np.random.randint(0, 2, size=16),
    'BED': np.random.randint(0, 2, size=16),
    'VaastuCompliant': np.random.randint(0, 2, size=16),
    'Microwave': np.random.randint(0, 2, size=16),
    'GolfCourse': np.random.randint(0, 2, size=16),
    'TV': np.random.randint(0, 2, size=16),
    'DiningTable': np.random.randint(0, 2, size=16),
    'Sofa': np.random.randint(0, 2, size=16),
    'Wardrobe': np.random.randint(0, 2, size=16),
    'Refrigerator': np.random.randint(0, 2, size=16)
}

# Create DataFrame for Khammam
df_khammam = pd.DataFrame(data_khammam)

# Save DataFrame to CSV
df_khammam.to_csv('khammam_dataset.csv', index=False)
