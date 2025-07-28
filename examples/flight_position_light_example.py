from flight_radar.factory import get_flight_radar_client
from flight_radar.models import LiveFlightPositionRequest

# Define your API token and the endpoint URL
API_TOKEN = 'your_api_token_here'
BASE_URL = 'https://fr24api.flightradar24.com/api'

# Create a flight radar service instance
service = get_flight_radar_client(
    base_url=BASE_URL,
    api_key=API_TOKEN,
)


# Define any request parameters
request = LiveFlightPositionRequest(bounds=(50.682, 46.218, 14.422, 22.243))


# Call the API to get the live flight positions
try:
    response = service.get_live_flight_positions(request)
    print('Live Flight Positions:')
    print(response)
except Exception as e:
    print(f'Error: {e}')
