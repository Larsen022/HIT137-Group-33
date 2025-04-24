# Import necessary modules
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

# Function to calculate average temperatures for each season
def calculate_average_temperatures():
    season_totals = defaultdict(float)  # Dictionary to store total temperatures for each season
    season_counts = defaultdict(int)   # Dictionary to store count of temperatures for each season

    # Iterate through all CSV files in the temperature_data folder
    for filename in os.listdir(TEMPERATURES_FOLDER):
        if filename.endswith(".csv"):  # Check if the file is a CSV file
            filepath = os.path.join(TEMPERATURES_FOLDER, filename)  # Get the full file path
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)  # Read the CSV file as a dictionary
                for row in reader:  # Iterate through each row in the CSV file
                    for month_name, temperature in row.items():  # Iterate through each column in the row
                        if month_name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:  # Check if the column is a month
                            for season, months in SEASONS.items():  # Map the month to its season
                                if month_name in months:
                                    season_totals[season] += float(temperature)  # Add the temperature to the season total
                                    season_counts[season] += 1  # Increment the count for the season

    # Calculate averages, skipping seasons with zero counts
    averages = {season: (season_totals[season] / season_counts[season]) if season_counts[season] > 0 else 0 for season in SEASONS}
    
    # Save the averages to a file
    with open("average_temp.txt", "w") as file:
        for season, avg_temp in averages.items():
            file.write(f"{season}: {avg_temp:.2f}\n")  # Write the average temperature for each season to the file

# Function to find the station with the largest temperature range
def find_largest_temperature_range_station():
    station_ranges = {}  # Dictionary to store the temperature range for each station

    # Iterate through all CSV files
    for filename in os.listdir(TEMPERATURES_FOLDER):
        if filename.endswith(".csv"):  # Check if the file is a CSV file
            filepath = os.path.join(TEMPERATURES_FOLDER, filename)  # Get the full file path
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)  # Read the CSV file as a dictionary
                for row in reader:  # Iterate through each row in the CSV file
                    station = row["STATION_NAME"]  # Get the station name from the row
                    for month_name, temperature in row.items():  # Iterate through each column in the row
                        if month_name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:  # Check if the column is a month
                            temperature = float(temperature)  # Convert the temperature to a float
                            if station not in station_ranges:  # Check if the station is not already in the dictionary
                                station_ranges[station] = {"min": temperature, "max": temperature}  # Initialize the min and max temperatures for the station
                            else:
                                station_ranges[station]["min"] = min(station_ranges[station]["min"], temperature)  # Update the min temperature for the station
                                station_ranges[station]["max"] = max(station_ranges[station]["max"], temperature)  # Update the max temperature for the station

    # Find the station(s) with the largest range
    largest_range = 0  # Initialize the largest range to 0
    largest_range_stations = []  # List to store the stations with the largest range
    for station, temps in station_ranges.items():  # Iterate through each station in the dictionary
        temp_range = temps["max"] - temps["min"]  # Calculate the temperature range for the station
        if temp_range > largest_range:  # Check if the range is larger than the current largest range
            largest_range = temp_range  # Update the largest range
            largest_range_stations = [station]  # Update the list of stations with the largest range
        elif temp_range == largest_range:  # Check if the range is equal to the current largest range
            largest_range_stations.append(station)  # Add the station to the list

    # Save the results to a file
    with open("largest_temp_range_station.txt", "w") as file:
        file.write(f"Largest Temperature Range: {largest_range:.2f}\n")  # Write the largest range to the file
        file.write("Stations:\n")  # Write the header for the stations
        for station in largest_range_stations:  # Iterate through each station in the list
            file.write(f"{station}\n")  # Write the station name to the file

# Function to find the warmest and coolest stations
def find_warmest_and_coolest_stations():
    station_totals = defaultdict(float)  # Dictionary to store the total temperatures for each station
    station_counts = defaultdict(int)  # Dictionary to store the count of temperatures for each station

    # Iterate through all CSV files
    for filename in os.listdir(TEMPERATURES_FOLDER):
        if filename.endswith(".csv"):  # Check if the file is a CSV file
            filepath = os.path.join(TEMPERATURES_FOLDER, filename)  # Get the full file path
            with open(filepath, "r") as file:
                reader = csv.DictReader(file)  # Read the CSV file as a dictionary
                for row in reader:  # Iterate through each row in the CSV file
                    station = row["STATION_NAME"]  # Get the station name from the row
                    for month_name, temperature in row.items():  # Iterate through each column in the row
                        if month_name in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:  # Check if the column is a month
                            station_totals[station] += float(temperature)  # Add the temperature to the station total
                            station_counts[station] += 1  # Increment the count for the station

    # Calculate averages for each station
    station_averages = {station: station_totals[station] / station_counts[station] for station in station_totals}  # Calculate the average temperature for each station

    # Find the warmest and coolest stations
    warmest_temp = max(station_averages.values())  # Find the highest average temperature
    coolest_temp = min(station_averages.values())  # Find the lowest average temperature
    warmest_stations = [station for station, avg in station_averages.items() if avg == warmest_temp]  # Find the stations with the highest average temperature
    coolest_stations = [station for station, avg in station_averages.items() if avg == coolest_temp]  # Find the stations with the lowest average temperature

    # Save the results to a file
    with open("warmest_and_coolest_station.txt", "w") as file:
        file.write(f"Warmest Temperature: {warmest_temp:.2f}\n")  # Write the highest temperature to the file
        file.write("Warmest Stations:\n")  # Write the header for the warmest stations
        for station in warmest_stations:  # Iterate through each station in the list
            file.write(f"{station}\n")  # Write the station name to the file
        file.write(f"Coolest Temperature: {coolest_temp:.2f}\n")  # Write the lowest temperature to the file
        file.write("Coolest Stations:\n")  # Write the header for the coolest stations
        for station in coolest_stations:  # Iterate through each station in the list
            file.write(f"{station}\n")  # Write the station name to the file

# Main function to execute the script
if __name__ == "__main__":
    calculate_average_temperatures()  # Call the function to calculate average temperatures
    find_largest_temperature_range_station()  # Call the function to find the largest temperature range station
    find_warmest_and_coolest_stations()  # Call the function to find the warmest and coolest stations