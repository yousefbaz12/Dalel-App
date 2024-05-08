import csv
import requests


def get_lat_lng(location):
    api_key = 'AIzaSyB5WMh66f-KcwdfUDYDjobHpGFYJ8-YUuI'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        print("Error: Unable to retrieve latitude and longitude.")
        return None, None


# Read the CSV file with addresses
with open('attractions.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Create a list to hold latitude and longitude data
lat_lng_data = []

# Iterate through the rows and get latitude and longitude for each address
for row in rows:
    address = row['Address']
    latitude, longitude = get_lat_lng(address)
    lat_lng_data.append({'latitude': latitude, 'longitude': longitude})

# Write latitude and longitude data to a new CSV file
with open('locations.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['latitude', 'longitude']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(lat_lng_data)
