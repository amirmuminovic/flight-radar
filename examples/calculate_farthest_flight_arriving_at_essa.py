from flight_radar.enums.enums import Direction
from flight_radar.factory import get_flight_radar_client
from flight_radar.models import LiveFlightPositionRequest
from geopy.distance import great_circle

from flight_radar.models.common import AirportWithDirection

# Define your API token and the endpoint URLs
API_TOKEN = 'your_api_token_here'
BASE_URL = 'https://fr24api.flightradar24.com/api'

# Get the flight radar service
service = get_flight_radar_client(
    base_url=BASE_URL,
    api_key=API_TOKEN,
)


### Step 1: Retrieve Flights Arriving at ESSA
# Define the query parameters
request = LiveFlightPositionRequest(
    airports=[
        AirportWithDirection(
            airport='ESSA',
            direction=Direction.INBOUND,
        )
    ]
)

# Call the API to retrieve flights
try:
    response = service.get_live_flight_positions(
        request,
    )

    # Filter out flights without an ETA
    flights_with_eta = [flight for flight in response if flight.eta is not None]
    # Order flights by ETA
    sorted_flights = sorted(flights_with_eta, key=lambda x: x.eta.timestamp() if x.eta else 0)
    print('Flights arriving at ESSA:')
    for flight in sorted_flights:
        print(flight)

except Exception as e:
    print(f'Error retrieving flights: {e}')
    exit()


# Step 2: Retrieve airport coordinates for ESSA
try:
    airport_response = service.get_airports('ESSA')
    destination_coords = (airport_response.lat, airport_response.lon)
    print('\nESSA Coordinates:')
    print(destination_coords)
except Exception as e:
    print(f'Error retrieving airport data: {e}')
    exit()


# Step 3: Calculate the Farthest Flight Using Great Circle Distance
# Function to calculate the great circle distance
def calculate_distance(coord1, coord2):
    return great_circle(coord1, coord2).kilometers


# Initialize variables to track the farthest flight
farthest_flight = None
max_distance = 0

# Calculate the distance for each flight
for flight in sorted_flights:
    origin_coords = (flight.lat, flight.lon)  # Current position of the flight
    # Calculate distance from the flight's current position to ESSA
    distance = calculate_distance(origin_coords, destination_coords)
    if distance > max_distance:
        max_distance = distance
        farthest_flight = flight

# Display the result
if farthest_flight:
    print(
        f'\nThe farthest flight is from {farthest_flight.orig_icao} to ESSA with a distance of {max_distance:.2f} km.'
    )
else:
    print('No flights found.')
