import pandas as pd
import os

folder_path = "C:\\Users\\Susmi\\Downloads\\HIT137 Assignment 2 S1 2025\\temperature_data"
all_ranges = []

# Looping through each file in the folder
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)

        # For each station, computing and storing the temperature range
        for _, row in df.iterrows():
            station_name = row['STATION_NAME']  # Make sure this matches your column name (check for case)
            temps = row[['January', 'February', 'March', 'April', 'May', 'June', 
                         'July', 'August', 'September', 'October', 'November', 'December']]
            
            max_temp = temps.max()
            min_temp = temps.min()
            temp_range = max_temp - min_temp

            all_ranges.append({
                'station': station_name,
                'range': temp_range
            })

# Converting to DataFrame for processing
ranges_df = pd.DataFrame(all_ranges)

# Finding maximum range value
max_range = ranges_df['range'].max()

# Filtering station(s) with maximum range
largest_range_stations = ranges_df[ranges_df['range'] == max_range]

# Writing to the file
with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"Largest temperature range: {max_range:.2f}°C\n")
    f.write("Station(s) with the largest range:\n")
    for station in largest_range_stations['station'].unique():
        f.write(f"- {station}\n")

print("Result saved to 'largest_temp_range_station.txt'")