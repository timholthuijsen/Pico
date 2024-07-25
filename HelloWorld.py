# Importing the library
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Define the address to geocode
address = "1600 Amphitheatre Parkway, Mountain View, CA"

# Geocode the address
location = geolocator.geocode(address)

# Display the results
print("Address:", address)
print("Latitude and Longitude:", (location.latitude, location.longitude))
