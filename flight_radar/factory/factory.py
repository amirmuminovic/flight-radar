import os
from requests import Session
from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.services.service import FlightRadarClient


def get_flight_radar_client(  # pragma: no cover
    base_url: str = os.getenv('FLIGHT_RADAR_BASE_URL', ''),
    api_key: str = os.getenv('FLIGHT_RADAR_API_KEY', ''),
) -> FlightRadarClient:
    """
    Factory function to create a FlightRadarClient instance.

    Args:
        base_url: The base URL of the Flight Radar API.
        api_key: The API key for the Flight Radar API.

    Returns:
        An instance of the FlightRadarClient.
    """
    session = Session()
    api_client = FlightRadarApiClient(session=session, base_url=base_url, api_key=api_key)

    return FlightRadarClient(api_client)
