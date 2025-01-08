import pandas as pd
import numpy as np

# Define the data
data = {
    'Area': [1500, 1800, 1200, 2000, 1600, 1700, 1400, 1900, 1750, 1850, 1300, 1950, 1550, 1650, 1450, 1700, 1600, 1500, 1800, 1200, 2000, 1600, 1700],
    'Price': [5500000, 6500000, 4200000, 7200000, 6000000, 4800000, 5200000, 6900000, 5800000, 6800000, 4500000, 7100000, 5900000, 5400000, 5300000, 6300000, 6000000, 5500000, 6500000, 4200000, 7200000, 6000000, 6300000],
    'Location': ['Subedari', 'Hanamkonda', 'Kazipet', 'Bheemaram', 'Waradhanapet', 'Subedari', 'Hanamkonda', 'Bheemaram', 'Kazipet', 'Subedari', 'Hanamkonda', 'Bheemaram', 'Waradhanapet', 'Kazipet', 'Subedari', 'Hanamkonda', 'Bheemaram', 'Balasamudram', 'Nakalagutta', 'Chinthagattu', 'Yerragattu Gutta', 'Rampur', 'Hasanparthy'],
    'No. of Bedrooms': [3, 4, 2, 3, 3, 2, 3, 4, 3, 4, 2, 3, 3, 2, 3, 4, 3, 3, 4, 2, 3, 3, 4],
    'Resale': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    'MaintenanceStaff': np.random.randint(0, 2, size=23),
    'Gymnasium': np.random.randint(0, 2, size=23),
    'SwimmingPool': np.random.randint(0, 2, size=23),
    'LandscapedGardens': np.random.randint(0, 2, size=23),
    'JoggingTrack': np.random.randint(0, 2, size=23),
    'RainWaterHarvesting': np.random.randint(0, 2, size=23),
    'IndoorGames': np.random.randint(0, 2, size=23),
    'ShoppingMall': np.random.randint(0, 2, size=23),
    'Intercom': np.random.randint(0, 2, size=23),
    'SportsFacility': np.random.randint(0, 2, size=23),
    'ATM': np.random.randint(0, 2, size=23),
    'ClubHouse': np.random.randint(0, 2, size=23),
    'School': np.random.randint(0, 2, size=23),
    '24X7Security': np.random.randint(0, 2, size=23),
    'PowerBackup': np.random.randint(0, 2, size=23),
    'CarParking': np.random.randint(0, 2, size=23),
    'StaffQuarter': np.random.randint(0, 2, size=23),
    'Cafeteria': np.random.randint(0, 2, size=23),
    'MultipurposeRoom': np.random.randint(0, 2, size=23),
    'Hospital': np.random.randint(0, 2, size=23),
    'WashingMachine': np.random.randint(0, 2, size=23),
    'Gasconnection': np.random.randint(0, 2, size=23),
    'AC': np.random.randint(0, 2, size=23),
    'Wifi': np.random.randint(0, 2, size=23),
    'ChildrensPlayArea': np.random.randint(0, 2, size=23),
    'LiftAvailable': np.random.randint(0, 2, size=23),
    'BED': np.random.randint(0, 2, size=23),
    'VaastuCompliant': np.random.randint(0, 2, size=23),
    'Microwave': np.random.randint(0, 2, size=23),
    'GolfCourse': np.random.randint(0, 2, size=23),
    'TV': np.random.randint(0, 2, size=23),
    'DiningTable': np.random.randint(0, 2, size=23),
    'Sofa': np.random.randint(0, 2, size=23),
    'Wardrobe': np.random.randint(0, 2, size=23),
    'Refrigerator': np.random.randint(0, 2, size=23)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('warangal_dataset.csv', index=False)
