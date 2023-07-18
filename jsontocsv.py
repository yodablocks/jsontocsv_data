import json
import csv

# Read data from JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the desired information
features = data['features']

# Prepare CSV file
csv_file = open('data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Label', 'Longitude', 'Latitude'])  # Header row

# Write data to CSV
for feature in features:
    properties = feature['properties']
    label = properties['label']
    coordinates = feature['geometry']['coordinates']
    
    csv_writer.writerow([label, coordinates[0], coordinates[1]])

# Close the CSV file
csv_file.close()

print("Data saved to 'data.csv'")
