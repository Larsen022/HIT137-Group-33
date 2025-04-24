import os
import csv
from collections import defaultdict

# Define the path to the temperature data folder
TEMPERATURES_FOLDER = "temperature_data"

# Update SEASONS to map month names to seasons
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"]
}

def calculate_average_temperatures():
    season_totals = defaultdict(float)
    season_counts = defaultdict(int)

    # Iterate through all CSV files in the temperature_data folder
    for filename in os.listdir(TEMPERATURES_FOLDER):
        if filename.endswith(".csv"):
            filepath = os.path.join(TEMPERATURES_FOLDER, filename)
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    for month_name, temperature in row.items():
                        if month_name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
                            for season, months in SEASONS.items():
                                if month_name in months:
                                    season_totals[season] += float(temperature)
                                    season_counts[season] += 1

    # Calculate averages, skipping seasons with zero counts
    averages = {season: (season_totals[season] / season_counts[season]) if season_counts[season] > 0 else 0 for season in SEASONS}
    
    # Save to file
    with open("average_temp.txt", "w") as file:
        for season, avg_temp in averages.items():
            file.write(f"{season}: {avg_temp:.2f}\n")

def find_largest_temperature_range_station():
    station_ranges = {}

    # Iterate through all CSV files
    for filename in os.listdir(TEMPERATURES_FOLDER):
        if filename.endswith(".csv"):
            filepath = os.path.join(TEMPERATURES_FOLDER, filename)
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    station = row["STATION_NAME"]  # Updated to use the correct column name
                    for month_name, temperature in row.items():
                        if month_name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
                            temperature = float(temperature)
                            if station not in station_ranges:
                                station_ranges[station] = {"min": temperature, "max": temperature}
                            else:
                                station_ranges[station]["min"] = min(station_ranges[station]["min"], temperature)
                                station_ranges[station]["max"] = max(station_ranges[station]["max"], temperature)

    # Find the station(s) with the largest range
    largest_range = 0
    largest_range_stations = []
    for station, temps in station_ranges.items():
        temp_range = temps["max"] - temps["min"]
        if temp_range > largest_range:
            largest_range = temp_range
            largest_range_stations = [station]
        elif temp_range == largest_range:
            largest_range_stations.append(station)

    # Save to file
    with open("largest_temp_range_station.txt", "w") as file:
        file.write(f"Largest Temperature Range: {largest_range:.2f}\n")
        file.write("Stations:\n")
        for station in largest_range_stations:
            file.write(f"{station}\n")

def find_warmest_and_coolest_stations():
    station_totals = defaultdict(float)
    station_counts = defaultdict(int)

    # Iterate through all CSV files
    for filename in os.listdir(TEMPERATURES_FOLDER):
        if filename.endswith(".csv"):
            filepath = os.path.join(TEMPERATURES_FOLDER, filename)
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    station = row["STATION_NAME"]  # Updated to use the correct column name
                    for month_name, temperature in row.items():
                        if month_name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
                            station_totals[station] += float(temperature)
                            station_counts[station] += 1

    # Calculate averages
    station_averages = {station: station_totals[station] / station_counts[station] for station in station_totals}

    # Find warmest and coolest stations
    warmest_temp = max(station_averages.values())
    coolest_temp = min(station_averages.values())
    warmest_stations = [station for station, avg in station_averages.items() if avg == warmest_temp]
    coolest_stations = [station for station, avg in station_averages.items() if avg == coolest_temp]

    # Save to file
    with open("warmest_and_coolest_station.txt", "w") as file:
        file.write(f"Warmest Temperature: {warmest_temp:.2f}\n")
        file.write("Warmest Stations:\n")
        for station in warmest_stations:
            file.write(f"{station}\n")
        file.write(f"Coolest Temperature: {coolest_temp:.2f}\n")
        file.write("Coolest Stations:\n")
        for station in coolest_stations:
            file.write(f"{station}\n")

if __name__ == "__main__":
    calculate_average_temperatures()
    find_largest_temperature_range_station()
    find_warmest_and_coolest_stations()