import pandas as pd
import os
folder_path = "C:\\Users\\Susmi\\Downloads\\HIT137 Assignment 2 S1 2025\\temperature_data"
all_ranges = []

#looping through each file in the folder
for file in os.listdir(folder_path):
  if file.endswith(".csv"):
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)


# for each station, computing and storing the temperature range
for _, row in df.iterrows():
    STATION_NAME = row['STATION_NAME']
    temps = row[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]

    max_temp = temps.max()    # for maximum temperature
    min_temp = temps.min()    #for minimum temperature
    temp_range = max_temp - min_temp   #for temperature range

    all_ranges.append({
        'station': STATION_NAME,
        'range': temp_range
    })

# converting to dataframe for processing
ranges_df = pd.DataFrame(all_ranges)

# finding maximum range value
max_range = ranges_df['range'].max()

# filtering station with maximum range
largest_range_stations = ranges_df[ranges_df['range'] == max_range]

# writing to the file
with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"largest temperature range: {max_range:.2f} degree celcius\n")
    f.write("stations(s) with the largest range:\n")
    for station in largest_range_stations['station'].unique():
        f.write(f"- {station}\n")

